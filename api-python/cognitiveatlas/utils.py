#!/usr/bin/env python

"""

utils: part of the cognitive atlas package

functions for working with the cognitive atlas!


"""

import os
import json
import errno
import rdflib
import urllib2
import numpy as np
import pandas
from urllib2 import Request, urlopen, HTTPError

# File operations 
def mkdir_p(path):
  try:
      os.makedirs(path)
  except OSError as exc: # Python >2.5
    if exc.errno == errno.EEXIST and os.path.isdir(path):
      pass
    else: raise

def url_get(url):
  request = Request(url)
  response = urlopen(request)
  return response.read()

# Data Json (from file)
def read_json_file(file_path):
  filey = open(file_path,'rb')
  tmp = filey.readlines()
  return json.loads("\n".join(tmp))

# Data Json Object (from URL)
class DataJson:
  """DataJson: internal class for storing json, accessed by NeuroVault Object"""
  def __init__(self,url):
    self.url = url
    self.json = self.get_json()
    self.data = self.parse_json() 
    
  """Print json data fields"""
  def __str__(self):
    return "DataJson Object dj Includes <dj.data:dict,js.json:list,dj.fields:list,dj.url:str>"

  """Get raw json object"""
  def get_json(self):
    return urllib2.urlopen(self.url).read()
    
  """Parse a json object into a dictionary (key = fields) of dictionaries (key = file urls)"""
  def parse_json(self):
    if not self.json:
      self.json = self.get_json()
    return json.loads(self.json)

# Data RDF Object
class DataRDF:
  """DataRDF: internal class for storing rdf, accessed by cognitiveatlas"""
  def __init__(self,url):
    self.url = url
    self.rdf = self.get_rdf()
    self.triples = self.read_triples()
   
  """Get raw json object"""
  def get_rdf(self):
    ca_g = rdflib.Graph()
    return ca_g.parse(self.url)

  def save(self,output_name,data_format="rdf"):
    if data_format == "rdf":  
      tmp = self.rdf.serialize(format='n3')
      filey = open("%s.n3" % output_name,"wb")
      filey.writelines(tmp)
      filey.close()
    else:
      self.triples.to_csv("%s.tsv" % output_name,sep="\t")

  def read_triples(self):
    print "Reading triples into data frame..."
    tmp = pandas.DataFrame(columns=["subject","predicate","object"])
    count = 0
    for subj, pred, obj in self.rdf:
      tmp.loc[count] = [subj.encode("utf-8"),pred.encode("utf-8"),obj.encode("utf-8")]
      count += 1
    # Create a column without the url
    trm = [t.replace("http://www.cognitiveatlas.org/id/","") for t in tmp["subject"]]
    tmp["UID"] = trm
    tmp.columns = ["URL","TYPE","NAME","UID"]
    return tmp
