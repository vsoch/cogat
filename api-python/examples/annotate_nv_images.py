#!/usr/bin/python

# Get concepts, tasks, etc.
from cognitiveatlas import api, brainspell,views

# Get a data frame of contrasts from the tasks data frame
tasks = api.get_tasks_df(filters="http://www.w3.org/2004/02/skos/core#prefLabel")
# Note: this data is not exposed yet, this is just a dummy for now
contrasts = api.get_concepts_df(filters="http://www.w3.org/2004/02/skos/core#prefLabel")

# Here we want to get an image from NeuroVault using pyneurovault (should give us a doi or pmid)
# TODO: write function for pyneurovault

# May need to look up pmid from doi here

# For now we will use an example pmid from Roberto.
# Grab a brainspell article data structure (using NeuroVault pmid)
pmid = "16863694"
article = brainspell.get_article(pmid)

# Now we can open an annotation interface for each image we want to annotate
# This will let us search for tasks and select contrasts to add to the brainspell data structure
views.annotate_images(tasks=tasks,article=article,contrasts=contrasts)

# Saving happens with button click, but could obviously happen other ways! Woot!
