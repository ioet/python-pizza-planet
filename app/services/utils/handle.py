from flask import jsonify

def handle_response(response, error, success_code=200, not_found_code=404, bad_request_code=400):
    response = response if not error else {'error': error}
    status_code = success_code if not error else not_found_code if not response else bad_request_code
    return jsonify(response), status_code