#!/usr/bin/env python

"""

utils: part of the cognitive atlas package

functions for working with the cognitive atlas!


"""

import os
import json
import errno
import urllib2
import numpy as np
from urllib2 import Request, urlopen, HTTPError
import rdflib


# Data RDF Object

class DataRDF:
  """DataRDF: internal class for storing rdf, accessed by cognitiveatlas"""
  def __init__(self,url):
    self.url = url
    self.rdf = self.__get_rdf__()

    #self.ttl = self.__parse_ttl__() 
   
  """Get raw json object"""
  def __get_rdf__(self):
    ca_g = rdflib.Graph()
    return ca_g.parse(self.url)

  """This function should create a provenance (prov) from an RDF"""
  def __make_prov__():
    print "TODO: Not sure how to do this :P"
    
  """This function should create a provenance (prov) from an RDF"""
  def __parse_ttl__(self):
    if not self.rdf:
      self.raw = self.__get_rdf__()
    # TODOHere - we want to convert to turtle

  """This will save the xml (rdf file) as n3"""
  def save(ext="n3",output_name):
    if ext == "n3":
      tmp = self.rdf.serialize(format='n3')
      filey = open(output_name,"wb")
      filey.writelines(tmp)
      filey.close()


  def read_tripes(self,pred)
  # STOPPED HERE: TODO: Write a function that can take a term of interest and return
  # the identifier from the rdf.
  # learn here --> http://rdflib.readthedocs.org/en/latest/gettingstarted.html
  # here from Chris --> http://nidm.nidash.org/specs/nidm-results_020.html
  
   # Here is an example of a query OMG IT'S SPARQL-ish :O
        query = """
        prefix prov: <http://www.w3.org/ns/prov#>
        prefix nidm: <http://www.incf.org/ns/nidash/nidm#>
        prefix spm: <http://www.incf.org/ns/nidash/spm#>
        prefix fsl: <http://www.incf.org/ns/nidash/fsl#>
        prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?rdfLabel ?contrastName ?statFile ?statType WHERE {
         ?cid a nidm:ContrastMap ;
              nidm:contrastName ?contrastName ;
              prov:atLocation ?cfile .
         ?cea a nidm:ContrastEstimation .
         ?cid prov:wasGeneratedBy ?cea .
         ?sid a nidm:StatisticMap ;
              nidm:statisticType ?statType ;
              rdfs:label ?rdfLabel ;
              prov:atLocation ?statFile .
        }
        """
        

        # Here is an example of how to do the query (we should do this to get ids for our concepts
        c_results = nidm_g.query(query)
        for row in c_results.bindings:
            c_row = {}
            for key, val in sorted(row.items()):
                c_row[str(key)] = val.decode()
            self.contrasts.append(c_row)

        # uniquify contrast values by file
        self.contrasts = {v['statFile']:v for v in self.contrasts}.values()

        return self.contrasts

