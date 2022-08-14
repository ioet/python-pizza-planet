from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request

from ..controllers import ReportController
from .base import *

report = Blueprint('report', __name__)


@report.route('/', methods=GET)
def get_report():
    entities, error = ReportController.generate_report()
    response = entities if not error else {'error': error}
    status_code = 200 if entities else 404 if not error else 400
    return jsonify(response), status_code
