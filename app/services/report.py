from app.common.http_methods import GET
from flask import Blueprint

from ..common.utils import instance_controller
from ..controllers.report import ReportController

report = Blueprint('report', __name__)

@report.route('/', methods=GET)
def get_report():
    return instance_controller(ReportController.get())