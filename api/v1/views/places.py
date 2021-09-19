#!/usr/bin/python3
"""This module declares city routes"""
import models
from flask import jsonify, abort
from flask import request as req
from models.place import Place
from api.v1.views import app_views


@app_views.route('/cities/<city_id>/places', methods=['GET', 'POST'])
def place_objects(city_id):
    """Returns place objects as JSON response"""
    city = models.storage.get('City', city_id)
    if city is None:
        abort(404)

    if req.method == 'GET':
        places = [obj.to_dict() for obj in city.places]
        return jsonify(places)

    if req.method == 'POST':
        body = req.get_json()
        if body is None:
            abort(400, 'Not a JSON')
        if body.get('name', None) is None:
            abort(400, 'Missing name')
        if body.get('user_id', None) is None:
            abort(400, 'Missing user_id')

        user = model.storage.get('User', body.get('user_id'))
        if user is None:
            abort(404)

        place = Place(**body)
        place.city_id = city_id
        place.save()
        return jsonify(place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['GET', 'PUT', 'DELETE'])
def place_res(place_id):
    """Returns a Place object as JSON response"""
    place = models.storage.get('Place', place_id)
    if place is None:
        abort(404)

    if req.method == 'GET':
        return jsonify(place.to_dict())

    if req.method == 'PUT':
        place_json = req.get_json()
        if place_json is None:
            abort(400, 'Not a JSON')
        ignore = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']
        for key, val in place_json.items():
            if key not in ignore:
                place.__setattr__(key, val)
        models.storage.save()
        return jsonify(place.to_dict())

    if req.method == 'DELETE':
        place.delete()
        models.storage.save()
        return jsonify({})
