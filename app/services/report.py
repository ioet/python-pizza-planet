
from app.common.http_methods import GET
from flask import Blueprint, jsonify

from ..controllers import ReportController

report = Blueprint('report', __name__)


@report.route('/', methods=GET)
def get_report():
    most_requested_ingredient, error = ReportController.get_report()
    response = most_requested_ingredient if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code


@report.route('/ingredient', methods=GET)
def get_most_requested_ingredient():
    most_requested_ingredient, error = ReportController.get_most_requested_ingredient()
    response = most_requested_ingredient if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code


@report.route('/month', methods=GET)
def get_month_with_more_revenue():
    month_with_more_revenue, error = ReportController.get_month_with_more_revenue()
    response = month_with_more_revenue if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code


@report.route('/customer', methods=GET)
def get_best_customers():
    best_customers, error = ReportController.get_best_customers()
    response = best_customers if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code
