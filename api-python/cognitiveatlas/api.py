#!/usr/bin/env python

"""

api: part of the cognitive atlas package

functions for working with the cognitive atlas!


"""

import os
import json
import string
import urllib
import utils
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
  if filters: concepts.triples = filter_result(concepts.triples,filters,"TYPE") 
  return concepts.triples

# Note for all df functions - it will be faster to just retrieve the triples instead of rdf
def get_tasks_df(filters=None):
  tasks = DataRDF("http://www.cognitiveatlas.org/rdf/objects/all_tasks.rdf")
  if filters: tasks.triples = filter_result(tasks.triples,filters,"TYPE") 
  return tasks.triples

def get_disorders_df(filters=None):
  disorders = DataRDF("http://www.cognitiveatlas.org/rdf/objects/all_disorders.rdf")
  if filters: disorders.triples = filter_result(disorders.triples,filters,"TYPE") 
  return disorders.triples

def get_collections_df(filters=None):
  collections = DataRDF("http://www.cognitiveatlas.org/rdf/objects/all_collections.rdf")
  if filters: collections.triples = filter_result(collections.triples,filters,"TYPE") 
  return collections.triples

def get_conditions_dump(filters=None):
  pwd = os.path.dirname(utils.__file__)
  conditions=pandas.read_csv("%s/data/condition_2015-01-25.csv" %(pwd),sep=";")
  return conditions

def get_contrasts_dump(filters=None):
  pwd = os.path.dirname(utils.__file__)
  contrasts= pandas.read_csv("%s/data/contrast_2015-01-25.csv" %(pwd),sep=";")
  contrasts.columns = ["ID","ID_USER","UID","CONTRAST_TEXT","EVENT_STAMP"]
  return contrasts

"""Match tasks and conditions and put into a data frame based on match columns.
Tasks: seem to have tsk and trm ids, but they are unique.
""" 
def task_and_contrast(tasks,contrasts,join_column):
  return pandas.merge(tasks,contrasts, on=join_column, how='right')

def filter_result(triples_df,filters,column_id):
  if isinstance(filters,str): filters = [filters]  
  return triples_df[triples_df[column_id].isin(filters)] 

