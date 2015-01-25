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


def get_concepts_df(filters=None)
  concepts = DataRDF("http://www.cognitiveatlas.org/rdf/objects/all_concepts.rdf")
  if filters: concepts = filter_result(concepts,filters) 
  return concepts

def get_tasks_df(filters=None):
  tasks = DataRDF("http://www.cognitiveatlas.org/rdf/objects/all_tasks.rdf")
  if filters: tasks = filter_result(tasks,filters) 
  return tasks

def get_disorders_df():
  disorders = DataRDF("http://www.cognitiveatlas.org/rdf/objects/all_disorders.rdf")
  if filters: disorders = filter_result(disorders,filters) 
  return disorders

def get_collections_df():
  tasks = DataRDF("http://www.cognitiveatlas.org/rdf/objects/all_collections.rdf")
  if filters: collections = filter_result(collections,filters) 
  return collections

def filter_result(triples_df,filters):
  if isinstance(filters,str): filters = [filters]  
  return triples_df[triples_df['predicate'].isin(filters)] 

