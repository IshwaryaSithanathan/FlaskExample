# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:01:05 2017

@author: ishwarya
"""

import json
from pymongo import MongoClient

# Connect to mongo db
client = MongoClient('mongodb://localhost:27017/')
# create database
db=client.cargobase
# create collection 
datab = db.airportData

#Store into db one by one
with open("airports.json",  encoding='utf-8-sig') as f:  
   data=json.load(f)
   for item in data["airports"]:
       datab.insert(item)
       
#Mongo query to return all airport data with given country name       
#db.airportData.find({countryName:"Canada"})
