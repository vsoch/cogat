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
import numpy as np
import pandas as pd
import nibabel as nb
import numpy as np
from utils import DataJson

__author__ = ["Poldracklab","Vanessa Sochat"]
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2015/01/23 $"
__license__ = "BSD"


def annotate_images(tasks,article,contrasts):
  # Prepare tasks as dictionary
  task_keys = list(tasks["subject"])
  task_names = list(tasks["object"])
  task_list = "["
  for t in range(0,len(task_keys)-1):
    task_list = '%s{"name":"%s","id":"%s"},\n' %(task_list,task_names[t],task_keys[t])
  task_list = '%s{"name":"%s","id":"%s"}]\n' %(task_list,task_names[-1],task_keys[-1])

  # Add task_list to template

  # Add article to template

  # add contrasts to template
