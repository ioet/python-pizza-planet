from app.common.http_methods import GET
from flask import Blueprint
from operator import itemgetter
from app.common.utils import handle_response
from ..controllers import OrderController

report = Blueprint('report', __name__)


def get_most_repeated_ingredient(orders_list):
    ingredient_count = {}

    for order in orders_list:
        for ingredients in order['ingredientsDetail']:
            ingredient_name = ingredients['ingredient']['name']
            if ingredient_name in ingredient_count:
                ingredient_count[ingredient_name] += 1
            else:
                ingredient_count[ingredient_name] = 1

    most_repeated_ingredient = None
    max_count = 0

    for ingredient_name, count in ingredient_count.items():
        if count > max_count:
            max_count = count
            most_repeated_ingredient = ingredient_name

    return most_repeated_ingredient


def get_month_with_more_revenue(orders_list):
    month_revenue = {}

    for order in orders_list:
        month = order["date"].split('-')[1]
        orden_price = order["total_price"]
        if month in month_revenue:
            month_revenue[month] += orden_price
        else:
            month_revenue[month] = orden_price

    month_with_more_revenue = None
    max_revenue = 0

    for month, revenue in month_revenue.items():
        if revenue > max_revenue:
            max_revenue = revenue
            month_with_more_revenue = month

    return (month_with_more_revenue)


def get_top_three_customers(orders_list):
    customer_spent = {}

    for order in orders_list:
        client_name = order["client_name"]
        order_price = order["total_price"]
        if client_name in customer_spent:
            customer_spent[client_name] += order_price
        else:
            customer_spent[client_name] = order_price

    sorted_customer_spent = sorted(
        customer_spent.items(),
        key=itemgetter(1),
        reverse=True)

    top_three_customers = sorted_customer_spent[:3]

    return top_three_customers


@report.route('/', methods=GET)
def create_report():
    orders, error = OrderController.get_all()
    orders_list = handle_response(orders, error)
    print()
    return({
        'most_repeated_ingredient': get_most_repeated_ingredient(orders_list[0].json),
        'month_with_more_revenue': get_month_with_more_revenue(orders_list[0].json),
        'top_three_customer': get_top_three_customers(orders_list[0].json)
    })
