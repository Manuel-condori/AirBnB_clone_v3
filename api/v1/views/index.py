#!/usr/bin/python3
"""This module declares index routes"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def index():
    """Returns a JSON response"""
    return jsonify({"status": "OK"})
