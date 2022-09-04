from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request

from app.controllers.order import OrderController

report = Blueprint('report', __name__)


@report.route('/', methods=GET)
def create_report():
    orders, error = OrderController.get_report_data()
    response = orders if not error else {'error': error}
    status_code = 200 if orders else 404 if not error else 400
    return jsonify(response), status_code

