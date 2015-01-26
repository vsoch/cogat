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
import pandas
import nibabel as nb
import numpy as np
from utils import DataRDF

__author__ = ["Poldracklab","Vanessa Sochat"]
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2015/01/23 $"
__license__ = "BSD"


def get_concepts_df(filters=None):
  concepts = DataRDF("http://www.cognitiveatlas.org/rdf/objects/all_concepts.rdf")
  if filters: concepts.triples = filter_result(concepts.triples,filters) 
  return concepts.triples

def get_tasks_df(filters=None):
  tasks = DataRDF("http://www.cognitiveatlas.org/rdf/objects/all_tasks.rdf")
  if filters: tasks.triples = filter_result(tasks.triples,filters) 
  return tasks.triples

def get_disorders_df(filters=None):
  disorders = DataRDF("http://www.cognitiveatlas.org/rdf/objects/all_disorders.rdf")
  if filters: disorders.triples = filter_result(disorders.triples,filters) 
  return disorders.triples

def get_collections_df(filters=None):
  collections = DataRDF("http://www.cognitiveatlas.org/rdf/objects/all_collections.rdf")
  if filters: collections.triples = filter_result(collections.triples,filters) 
  return collections.triples

def filter_result(triples_df,filters):
  if isinstance(filters,str): filters = [filters]  
  return triples_df[triples_df['predicate'].isin(filters)] 

