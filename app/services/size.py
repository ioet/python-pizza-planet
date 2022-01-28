from app.common.http_methods import GET, POST, PUT
from flask import Blueprint

size = Blueprint('size', __name__)


@size.route('/', methods=POST)
def create_size():
    pass


@size.route('/', methods=PUT)
def update_size():
    pass


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    pass
