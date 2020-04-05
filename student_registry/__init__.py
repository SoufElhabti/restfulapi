import markdown 
import os
#import the framework

from flask import Flask 
from flask import g
from flask_restful import Resource, Api, reqparse
import shelve


####APP

app = Flask(__name__)

api = Api(app)





#Create an instance of Flask app 

#connect and define database 
def get_db():
	db = getattr(g,'_database',None)
	if db is None:
		db = g._database = shelve.open("students.db", flag='c')
	return db

@app.teardown_appcontext
def teardown_db(exception):
	db = getattr(g,'_database',None)
	if db is not None:
		db.close()


@app.route("/")



def index() :
	'''the flask documentation'''
	#open Readme file
	with open(os.path.dirname(app.root_path)+'/README.md','r') as markdown_file:
		#Reading the markdown file
		content = markdown_file.read()

		#convert to html
		return markdown.markdown(content)


class StudentList(Resource):
	def get(self):
		shelf = get_db()
		keys = list(shelf.keys())

		students = [] 

		for key in keys:
			students.append(shelf[key])

		return {'message':'Success','data':students}, 200

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('identifier', required=True)
		parser.add_argument('name', required=True)
		parser.add_argument('Branch', required=True)
		parser.add_argument('Address',required=True)

		#parse this into an object 
		args = parser.parse_args()
		shelf = get_db()
		shelf[args['identifier']] = args

		return {'message':'student registered','data':args},201

class Student(Resource):
	def get(self,identifier):
		shelf = get_db()

		#if key not found it returns 404 error status 
		if not (identifier in shelf):
			return {'message':'student not found','data':{}}, 404
		return {'message':'student found','data':shelf[identifier]}, 200

	def delete(self,identifier):
		shelf = get_db()
		#if key not found it returns 404 error status 
		if not (identifier in shelf):
			return {'message':'student not found','data':{}}, 404
		return '', 204



api.add_resource(StudentList,'/students')
api.add_resource(Student,'/student/<string:identifier>')


