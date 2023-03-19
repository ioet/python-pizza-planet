from app.common.generate_fake_data import main
from flask import Blueprint
from app.common.http_methods import GET

populate = Blueprint('populate', __name__)

@populate.route("/", methods=GET)
def populate_fake_data():
    main()
    return ("Database populated with fake data")
