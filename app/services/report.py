from app.common.http_methods import GET
from flask import Blueprint
from app.fakedata.generate_fake_data import main

report = Blueprint('report', __name__)

@report.before_app_first_request
def populate_fake_data():
    main()

@report.route('/', methods=GET)
def create_report():
    return 'create_report'