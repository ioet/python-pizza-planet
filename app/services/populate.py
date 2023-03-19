from app.common.generate_fake_data import main
from flask import Blueprint

populate = Blueprint('report', __name__)


@populate.before_app_first_request
def populate_fake_data():
    print('Populating fake data...')
    main()
