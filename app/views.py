from app import app
from py2neo import neo4j, cypher
from urlparse import urlparse
import re, json
from flask import Flask, Response, json, jsonify, request, Blueprint, render_template

@app.route('/')
@app.route('/index')
def index():
	return "Base --hello"
	
@app.route('/unity')
def unity():

	#callbackArguments = request.args['callback']
 
	# create DB connection
	db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")
	
	nodes = getNodes(db)
 
	result = {
		'nodes' : nodes
	}
 
	result = json.dumps(result)
 
	# GET Request Response
	#callbackWrapper = callbackArguments + "(" + unicode(result) + ")"
	#callbackWrapper = callbackArguments + "(" + jsonify(result) + ")" 
	#resp = Response(callbackWrapper, status = 200, mimetype = 'application/json') 

	return result

def getNodes(db):

	query_string = 'MATCH (game)-[:USES_MECHANIC]->(mechanic) WHERE mechanic.mechanic = "Trick-taking" RETURN game.bgg_name'

	data, metadata = cypher.execute(db, query_string)

	json_returner =[]
	
	for r in data:
		json_returner.append(r[0])
		
	#print json_returner	
	return json_returner