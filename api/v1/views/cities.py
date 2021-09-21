#!/usr/bin/python3
"""This module declares index routes"""
import models
from flask import jsonify, abort
from flask import request as req
from models.city import City
from api.v1.views import app_views
from flasgger import swag_from


@swag_from('defs/cities/get.yml', methods=['GET'])
@swag_from('defs/cities/post.yml', methods=['POST'])
@app_views.route('/states/<state_id>/cities', methods=['GET', 'POST'])
def state_cities(state_id):
    """Returns city objects as JSON response"""
    state = models.storage.get('State', state_id)
    if state is None:
        abort(404)

    if req.method == 'GET':
        cities = [ct.to_dict() for ct in state.cities]
        return jsonify(cities)

    if req.method == 'POST':
        body = req.get_json()
        if body is None:
            abort(400, 'Not a JSON')
        if body.get('name', None) is None:
            abort(400, 'Missing name')
        city = City(**body)
        city.state_id = state_id
        city.save()
        return jsonify(city.to_dict()), 201


@swag_from('defs/cities/get_id.yml', methods=['GET'])
@swag_from('defs/cities/put_id.yml', methods=['PUT'])
@swag_from('defs/cities/delete_id.yml', methods=['DELETE'])
@app_views.route('/cities/<city_id>', methods=['GET', 'PUT', 'DELETE'])
def city_resource(city_id):
    """Returns a City object as JSON response"""
    city = models.storage.get('City', city_id)
    if city is None:
        abort(404)

    if req.method == 'GET':
        return jsonify(city.to_dict())

    if req.method == 'PUT':
        city_json = req.get_json()
        if city_json is None:
            abort(400, 'Not a JSON')
        ignore = ['id', 'state_id', 'created_at', 'updated_at']
        for key, val in city_json.items():
            if key not in ignore:
                city.__setattr__(key, val)
        models.storage.save()
        return jsonify(city.to_dict())

    if req.method == 'DELETE':
        city.delete()
        models.storage.save()
        return jsonify({})
