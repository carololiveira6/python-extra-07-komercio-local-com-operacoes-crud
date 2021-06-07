from flask import Flask, jsonify, request
from flask_cors import CORS
from services.populate_services import ProductService
from database import DATABASE_PATH
import csv, os
from os.path import exists

FIELDNAMES = ["id", "name", "price"]

app = Flask(__name__)
CORS(app)

