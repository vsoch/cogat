#!/usr/bin/python

from cognitiveatlas import api, brainspell,views


# COGNITIVE ATLAS: Get data frames with tasks and contrasts
tasks = api.get_tasks_df(filters="http://www.w3.org/2004/02/skos/core#prefLabel")
# Note: this data is not exposed yet, this is just a dummy for now
contrasts = api.get_concepts_df(filters="http://www.w3.org/2004/02/skos/core#prefLabel")


# NEUROVAULT:
# Here we will get an image from NeuroVault using pyneurovault (should give us a doi or pmid)
# TODO: write function for pyneurovault api (may need to look up pmid from doi if not available)


# BRAINSPELL: grab a brainspell article data structure (using NeuroVault pmid)
# For now we will use an example pmid from Roberto.
pmid = "16863694"
article = brainspell.get_article(pmid)

# ANNOTATE
# Now we can open an annotation interface for each image we want to annotate [eg, a loop could be here]
# This will let us search for tasks and select contrasts to add to the brainspell data structure, and save the new data structure
views.annotate_images(tasks=tasks,article=article,contrasts=contrasts)
