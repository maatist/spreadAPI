from flask import Flask
from flask_restx import Api
from .routes import api as ns1

app = Flask(__name__)
api = Api(app)

api.add_namespace(ns1, path='/spreadAPI')