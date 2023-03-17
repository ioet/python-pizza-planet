from flask import jsonify

def check_required_keys(keys: tuple, element: dict):
    return all(element.get(key) for key in keys)

def handle_response(service_response, error):
    SUCCESS_CODE = 200
    NOT_FOUND_CODE = 404
    BAD_REQUEST_CODE = 400

    response = service_response if not error else {'error': error}
    status_code = SUCCESS_CODE if response else NOT_FOUND_CODE if not error else BAD_REQUEST_CODE
    return jsonify(response), status_code