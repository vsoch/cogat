#!/usr/bin/env python

"""

api: part of the cognitive atlas package

functions for working with the cognitive atlas!


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
from utils import DataRDF

__author__ = ["Poldracklab","Vanessa Sochat"]
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2015/01/23 $"
__license__ = "BSD"

def get_concepts_df():
   """Get concepts data frame"""
   concepts = DataRDF("http://www.cognitiveatlas.org/rdf/objects/all_concepts.rdf")

def get_tasks_df():
   """Get tasks data frame"""


def get_disorders_df():
   """Get disorders data frame"""


def get_collections_df():
   """Get collections data frame"""


 images = DataJson("http://neurovault.org/api/images/?format=json")
    images.data['collection'] = images.data['collection'].apply(lambda x: int(x.split("/")[-2]))
    images.data['image_id'] = images.data['url'].apply(lambda x: int(x.split("/")[-2]))
    images.data.rename(columns={'collection':'collection_id'}, inplace=True)
   

