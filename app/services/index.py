from flask import Blueprint, jsonify
from app.common.http_methods import GET

from ..factories.factories import fill_data_base
from ..controllers import IndexController

index = Blueprint('index', __name__)


@index.route('/', methods=GET)
def get_index():
    is_database_up, error = IndexController.test_connection()
    return jsonify(
        {'version': '0.0.2', 'status': 'up' if is_database_up else 'down', 'error': error}
    )


@index.route('/fill_data_base', methods=GET)
def seed_database():
    try:
        fill_data_base()
        return jsonify({'working': 'hard'})
    except Exception:  # pylint: disable=broad-except
        return jsonify({'error': 'something went wrong'})
