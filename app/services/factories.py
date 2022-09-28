from flask import Blueprint, jsonify
from app.common.http_methods import GET

from ..factories.factories import fill_data_base

factories = Blueprint('factories', __name__)


@factories.route('/fill_data_base', methods=GET)
def seed_database():
    try:
        fill_data_base()
        return jsonify({'working': 'hard'})
    except Exception:  # pylint: disable=broad-except
        return jsonify({'error': "the database has been filled"})
