from flask import jsonify

def check_required_keys(keys: tuple, element: dict):
    return all(element.get(key) for key in keys)

def instance_controller(controller):
    entity, error = controller
    response = entity if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code
