#!/usr/bin/python

# Get concepts, tasks, etc.
from cognitiveatlas import api, brainspell, template, views

# Get a data frame of contrasts from the tasks data frame
# Note: this data is not exposed yet, this is just a dummy for now
tasks = api.get_tasks_df(filters="http://www.w3.org/2004/02/skos/core#prefLabel")
contrasts = api.get_concepts_df(filters="http://www.w3.org/2004/02/skos/core#prefLabel")

# Here we want to get an image from NeuroVault using pyneurovault (should give us a doi or pmid)
# TODO: write function for pyneurovault

# May need to look up pmid from doi here

# Grab a brainspell article data structure (using NeuroVault pmid)
pmid = "16863694"
article = brainspell.get_article(pmid)

# Now we need to test an interface to select contasts to associate with the image
views.annotate_images(tasks=tasks,article=article,contrasts=contrasts)
# IN PROGRESS!

# Add contrasts to data structure when user is done

# Save data structure



