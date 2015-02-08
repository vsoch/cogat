#!/usr/bin/python

from cognitiveatlas import api, brainspell,views,utils
from pyneurovault import api as nvapi 
from pyneurovault import pubmed as pm
import pandas

# COGNITIVE ATLAS: Get data frames with tasks and contrasts
tasks = api.get_tasks_df(filters="http://www.w3.org/2004/02/skos/core#prefLabel")
# We only have data dump for now for conditions
contrasts = api.get_contrasts_dump()

# NEUROVAULT: get all openfmri studies
nv = nvapi.NeuroVault()
df = nv.get_images_with_collections_df()
openfmri = nv.search(df=df,column_name="description_collection",search_string="OpenfMRI")
openfmri = openfmri[openfmri["DOI"].isnull()==False]
collections = nvapi.collections_from_dois(openfmri["DOI"].unique())
images = nvapi.images_from_collections(collections)
# TODO: the above should return one clean object with both these things.

# PUBMED:
# Look up pmids for each collection
pubmed = pm.Pubmed(email="vsochat@stanford.edu")
pmids = []
for collection in collections:
  article = pubmed.get_single_article(collection.data["DOI"])
  pmid = article.get_pmid()
  pmids.append(pmid)

# BRAINSPELL: grab a brainspell article data structure for each pmid [this could be any data structure]
brainspells = dict()
for pmid in pmids:
  article = brainspell.get_article(pmid)
  if article: brainspells[pmid] = article.json

# brainspell has bug that it doesn't comment out "", so we need to read in some from file
from cognitiveatlas.utils import read_text_file
brainspells["17409238"] = read_text_file("examples/data/17409238.json")
brainspells["17919929"] = read_text_file("examples/data/17919929.json")
brainspells["19289173"] = read_text_file("examples/data/19289173.json")

# will save temporary for now
pickle.dump(brainspells,open("examples/data/brainspells.pkl","wb"))

# ANNOTATE
# Now we can open an annotation interface for each image we want to annotate
# This will let us search for tasks and select contrasts to add to the brainspell data structure, and save the new data structure
for i in range(0,len(pmids)):
  pmid = pmids[i]
  article = brainspells[pmid]
  imageset = images[i]
  for image in imageset:
    views.annotate_images_contrasts_json(tasks=tasks,contrasts=contrasts,article=article,image=image)

