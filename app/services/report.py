from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request

from ..controllers import ReportController

report = Blueprint('report', __name__)


@report.route('/', methods=GET)
def get_most_required_ingredient():
    reportIngredient = ReportController.get_most_required()
    reportBeverage = ReportController.get_beverage_most_required()
    reportClient = ReportController.get_customers_who_buy_the_most()
    reportMonth  = ReportController.get_month_with_most_sales()
    return jsonify({'ingrediente': dict(row) for row in reportIngredient},
    {'beverage': dict(row) for row in reportBeverage}, {'clients': [dict(row) for row in reportClient]}, 
    {'month': dict(row) for row in reportMonth})
    