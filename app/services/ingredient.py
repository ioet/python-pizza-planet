from app.common.http_methods import GET, POST, PUT
from flask import Blueprint

ingredient = Blueprint('ingredient', __name__)


@ingredient.route('/', methods=POST)
def create_ingredient():
    pass


@ingredient.route('/', methods=PUT)
def update_ingredient():
    pass


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    pass


@ingredient.route('/', methods=GET)
def get_ingredients():
    pass
