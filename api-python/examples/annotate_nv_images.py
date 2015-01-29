#!/usr/bin/python

from cognitiveatlas import api, brainspell,views,utils
from pyneurovault import api as nvapi 
from pyneurovault import pubmed as pm
import pandas

# COGNITIVE ATLAS: Get data frames with tasks and contrasts
tasks = api.get_tasks_df(filters="http://www.w3.org/2004/02/skos/core#prefLabel")
# We only have data dump for now for conditions
contrasts = api.get_contrasts_dump()

# NEUROVAULT:
# Here is metadata about the openfmri experiments - we will be getting statistical maps from NeuroVault
openfmri = pandas.read_csv("examples/data/openfmri.txt",sep="\t")
openfmri = openfmri[openfmri["doi_or_pmid"].isnull()==False] # get rid of empty
openfmri = openfmri[openfmri["doi_or_pmid"].str.contains("/")] # NeuroVault can only lookup by doi
collections = nvapi.collections_from_dois(openfmri["doi_or_pmid"])
collections = [collection for collection in collections if collection.data is not None]
images = nvapi.images_from_collections(collections)
# TODO: the above should return one clean object with both these things.


# PUBMED:
# Look up pmids for each collection
pubmed = pm.Pubmed(email="vsochat@stanford.edu")
articles = []; pmids = []
for collection in collections:
  article = pubmed.get_single_article(collection.data["DOI"])
  articles.append(article)
  pmids.append(article.get_pmid())

# BRAINSPELL: grab a brainspell article data structure for each pmid 
brainspells = [brainspell.get_article(pmid) for pmid in pmids]
# Or grab a flat json file of your choice
brainspells = [utils.read_json_file("examples/data/article.json")]

# ANNOTATE
# Now we can open an annotation interface for each image we want to annotate
# This will let us search for tasks and select contrasts to add to the brainspell data structure, and save the new data structure
for i in range(0,len(images)):
  article = brainspells[i]
  imageset = images[i]
  for image in imageset:
    views.annotate_images(tasks=tasks,contrasts=contrasts,article=article,image=image)

