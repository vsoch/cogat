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
from utils import DataJson
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
  raw_input("Press Enter to finish...")

# Make temporary directory
@contextlib.contextmanager
def make_tmp_folder():
  temp_dir = tempfile.mkdtemp()
  yield temp_dir
  shutil.rmtree(temp_dir)

def annotate_images(tasks,article,contrasts):
  # Prepare tasks as dictionary
  task_keys = list(tasks["subject"])
  task_names = list(tasks["object"])
  task_list = "["
  for t in range(0,len(task_keys)-1):
    task_list = '%s{"name":"%s","id":"%s"},\n' %(task_list,task_names[t],task_keys[t])
  task_list = '%s{"name":"%s","id":"%s"}]\n' %(task_list,task_names[-1],task_keys[-1])

  # Get template 
  template = get_template("annotate_images")

  # Add task_list to template
  template = add_string({"CA_TASKS":task_list},template)

  # Add article to template
  template = add_string({"BRAINSPELL_ARTICLE":json.dumps(article.data)},template)

  # add contrasts to template
  # will do when we get them!
  view(template)
