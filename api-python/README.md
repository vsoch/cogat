# Cognitive Atlas Python API

*in development*

This API will allow python access to the RDF data structures in the cognitive atlas, including:

- tasks
- concepts
- disorders
- collections
- contrasts (soon)

as well as tools to annotate data, and integrate with brain imaging databases (NeuroVault) as well as annotation platforms (brainspell).  For example, [this workflow](examples/annotate_nv_images.py) shows doing the following:

- grab contrasts and tasks from the cognitive atlas (the ontology)
- grab images we want to label from NeuroVault (the data)
- grab the metadata for the image from brainspell (the data structure)
- open up interactive web interface to search and do tagging
- click save button to output modified data structure

A demo of the annotation interface that pops up is [available here](http://www.vbmis.com/bmi/project/cogatlas/annotate.html)


