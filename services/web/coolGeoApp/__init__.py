from flask import Flask
import psycopg2
import os

app = Flask(__name__)

import coolGeoApp.views


