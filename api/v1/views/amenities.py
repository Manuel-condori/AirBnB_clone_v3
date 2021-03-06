#!/usr/bin/python3
"""This module declares city routes"""
import models
from flask import jsonify, abort
from flask import request as req
from models.amenity import Amenity
from api.v1.views import app_views
from flasgger import swag_from


@swag_from('defs/amenities/get.yml', methods=['GET'])
@swag_from('defs/amenities/post.yml', methods=['POST'])
@app_views.route('/amenities', methods=['GET', 'POST'])
def amenity_objects():
    """Returns amenity objects as JSON response"""
    if req.method == 'GET':
        amenities = models.storage.all('Amenity')
        amenities = [am.to_dict() for am in amenities.values()]
        return jsonify(amenities)

    if req.method == 'POST':
        body = req.get_json()
        if body is None:
            abort(400, 'Not a JSON')
        if body.get('name', None) is None:
            abort(400, 'Missing name')
        amenity = Amenity(**body)
        amenity.save()
        return jsonify(amenity.to_dict()), 201


@swag_from('defs/amenities/get_id.yml', methods=['GET'])
@swag_from('defs/amenities/put_id.yml', methods=['PUT'])
@swag_from('defs/amenities/delete_id.yml', methods=['DELETE'])
@app_views.route('/amenities/<amenity_id>', methods=['GET', 'PUT', 'DELETE'])
def amenity_res(amenity_id):
    """Returns a Amenity object as JSON response"""
    amenity = models.storage.get('Amenity', amenity_id)
    if amenity is None:
        abort(404)

    if req.method == 'GET':
        return jsonify(amenity.to_dict())

    if req.method == 'PUT':
        amenity_json = req.get_json()
        if amenity_json is None:
            abort(400, 'Not a JSON')
        ignore = ['id', 'created_at', 'updated_at']
        for key, val in amenity_json.items():
            if key not in ignore:
                amenity.__setattr__(key, val)
        models.storage.save()
        return jsonify(amenity.to_dict())

    if req.method == 'DELETE':
        amenity.delete()
        models.storage.save()
        return jsonify({})
