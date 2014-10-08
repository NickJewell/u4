from app import app
from py2neo.neo4j import GraphDatabaseService, CypherQuery
from urlparse import urlparse
import re, json
from flask import Flask, Response, json, jsonify, request, Blueprint, render_template

graph = GraphDatabaseService("http://localhost:7474/db/data/")

@app.route('/')
@app.route('/index')
def index():
	return "Base --hello"
	
@app.route('/unity')
def unity():

	results = CypherQuery(graph, 'MATCH (game)-[:USES_MECHANIC]->(mechanic) WHERE mechanic.mechanic = "Trick-taking" RETURN game.bgg_name order by game.bgg_name').execute()
	return render_template("games.html", games=results)
