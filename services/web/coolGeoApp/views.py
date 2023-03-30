from flask import jsonify
from coolGeoApp import app

@app.route('/')
def index():
    return jsonify(hello='world')