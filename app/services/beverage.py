from flask import Blueprint, jsonify, request

from ..controllers.beverage import BeverageController

beverage = Blueprint('beverage', __name__)


@beverage.route('/', methods=['POST'])
def create_beverage():
    beverage, error = BeverageController.create(request.json)
    if error:
        return jsonify({'error': error}), 400
    return jsonify(beverage), 200


@beverage.route('/', methods=['PUT'])
def update_beverage():
    beverage, error = BeverageController.update(request.json)
    if error:
        return jsonify({'error': error}), 400
    return jsonify(beverage), 200


@beverage.route('/id/<int:_id>', methods=['GET'])
def get_beverage_by_id(_id):
    beverage, error = BeverageController.get_by_id(_id)
    if error:
        return jsonify({'error': error}), 400
    if not beverage:
        return jsonify({'error': 'Beverage not found'}), 404
    return jsonify(beverage), 200


@beverage.route('/', methods=['GET'])
def get_beverages():
    beverages, error = BeverageController.get_all()
    if error:
        return jsonify({'error': error}), 400
    if not beverages:
        return jsonify({'error': 'No beverages found'}), 404
    return jsonify(beverages), 200
