#!/usr/bin/python3
"""This module declares index routes"""
import models
from flask import jsonify
from api.v1.views import app_views

classes = {
    "Amenity": 'amenities',
    "City": 'cities',
    "Place": 'places',
    "Review": 'reviews',
    "State": 'states',
    "User": 'users'
}


@app_views.route('/status')
def index():
    """Returns a JSON response"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def count():
    """Returns a JSON response"""
    data = {}
    for cls, nick in classes.items():
        data[nick] = models.storage.count(cls)
    return jsonify(data)
