
from datetime import datetime
from flask import Blueprint, jsonify
from app.common.http_methods import GET
from app.controllers.ingredient import IngredientController
from app.controllers.order import OrderController

report = Blueprint('report', __name__)


@report.route("/best_ingredients", methods=GET)
def get_best_ingredients():
    ingredients_id = OrderController.get_best_ingredients()
    ingredients = {str(_id['_id']): None for _id in ingredients_id}
    entity, error = IngredientController.get_by_id_list(ingredients.keys())
    response = entity if not error else {'error': error}
    status_code = 200 if not error else 400
    if not error:
        for _ingredient in entity:
            ingredients[str(_ingredient.get_id())] = {'name': _ingredient.name}
        return jsonify(list(ingredients.values())), status_code
    return jsonify(response), status_code


@report.route("/best_customers", methods=GET)
def get_best_customers():
    customers = OrderController.get_best_customers()
    return jsonify(customers), 200


@report.route("/best_months", methods=GET)
def get_best_months():
    data = OrderController.get_best_months()
    parsed_dates = map(lambda _data: {'date': __parse_datetime_to_month_year(_data['date'])}, data)
    return jsonify(list(parsed_dates)), 200


def __parse_datetime_to_month_year(date: str) -> str:
    time_format = '%Y-%m-%dT%H:%M:%S'
    date = datetime.strptime(date, time_format)
    return f'{date.year}-{date.month}'
