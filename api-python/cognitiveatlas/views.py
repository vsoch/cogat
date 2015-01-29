#!/usr/bin/env python

"""

views: part of the cognitive atlas package

functions for doing annotations, viewing data, etc.


"""

import os
import json
import string
import urllib
import urllib2
import shutil
import tempfile
import contextlib
import webbrowser
import numpy as np
import pandas as pd
import nibabel as nb
from template import get_template, add_string

__author__ = ["Poldracklab","Vanessa Sochat"]
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2015/01/23 $"
__license__ = "BSD"


'''View code in temporary browser!'''
def view(html_snippet):
  with make_tmp_folder() as tmp_dir:  
    # Write to temporary file
    tmp_file = "%s/cogannotate.html" %(tmp_dir)
    internal_view(html_snippet,tmp_file)

'''Internal view function'''
def internal_view(html_snippet,tmp_file):
  html_file = open(tmp_file,'wb')
  html_file.writelines(html_snippet)
  html_file.close()
  url = 'file://%s' %(tmp_file)
  webbrowser.open_new_tab(url)
  raw_input("Press Enter for next/to finish...")

# Make temporary directory
@contextlib.contextmanager
def make_tmp_folder():
  temp_dir = tempfile.mkdtemp()
  yield temp_dir
  shutil.rmtree(temp_dir)

def annotate_images(tasks,contrasts,article,image):
  # Prepare lookup table for contrasts
  task_keys = list(tasks["UID"])
  task_names = list(tasks["NAME"]) 
  lookup = dict()
  for task in task_keys:
    subset = contrasts[contrasts["UID"].isin([task])]
    tmp = ['{"conname":"%s","conid":"%s"}' %(item[1]["CONTRAST_TEXT"],item[1]["ID"]) for item in subset.iterrows()]
    if tmp: lookup[task] = tmp # only include if defined contrasts

  # Removed tasks without contrasts
  tasks = tasks[tasks["UID"].isin(lookup.keys())]
  task_keys = list(tasks["UID"])
  task_names = list(tasks["NAME"]) 
  task_list = "["
  for t in range(0,len(task_keys)-1):
    task_list = '%s{"name":"%s","id":"%s","contrasts":[%s]},\n' %(task_list,task_names[t],task_keys[t],",".join(lookup[task_keys[t]]))
  task_list = '%s{"name":"%s","id":"%s","contrasts":[%s]}]\n' %(task_list,task_names[-1],task_keys[-1],",".join(lookup[task_keys[-1]]))

  # Image info
  image_id = str(image["url"].replace("http://neurovault.org/images/","")[:-1])
  image_info = '{"name":"%s","file":"%s","collection_key":"%s","image_key":"%s"}' %(image["file"],image["url"],image["collection"],image_id)
  image_info = image_info.encode("utf-8")

  # Get template 
  template = get_template("annotate_images")
  # Add task_list to template
  template = add_string({"CA_TASKS":task_list},template)
  # Add image_info to template
  template = add_string({"IMAGE_INFO":image_info},template)
  # Add article to template
  template = add_string({"BRAINSPELL_ARTICLE":article},template)
  view(template)
