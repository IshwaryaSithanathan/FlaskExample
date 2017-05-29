from flask import Flask, Response, render_template, request
from flask import jsonify
from pymongo import MongoClient

# Connect to mongo db
client = MongoClient('mongodb://localhost:27017/')
# create database
db=client.cargobase
# create collection 
datab = db.airportData

app = Flask(__name__)

#Home page
@app.route('/countries')
def home_page():
    countries = datab.distinct("countryName")
    return render_template('airportSearch.html',countries=countries)

#Get airport names
@app.route('/get_airport_names')
def get_airport_names():
    country = request.args.get('param')
    airports = datab.find({"countryName":country}).distinct("name")
    return jsonify(json_list=airports) 
