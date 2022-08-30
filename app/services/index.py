from app.common.http_methods import GET
from flask import Blueprint, jsonify

from ..controllers import IndexController

index = Blueprint('index', __name__)


@index.route('/', methods=GET)
def get_index():
    is_database_up, error = IndexController.test_connection()
    return jsonify(
        {
            'version': '0.0.2',
            'status': 'up' if is_database_up else 'down',
            'error': error,
        }
    )
