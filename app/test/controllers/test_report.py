import pytest

from app.controllers.order import OrderController
from app.controllers.report import ReportController


def test_get_all(app, create_repeted_clients_and_ingredients_order):

    orders, most_repeated_client, most_repeated_ingredient_id, second_most_repeated_client, third_most_repeated_client = create_repeted_clients_and_ingredients_order
    created_order_result = []
    for order in orders:
        created_order, error = OrderController.create(order)
        pytest.assume(error is None)
        created_order_result.append(created_order)
    report_from_db, error = ReportController.get_all()
    pytest.assume(error is None)
    pytest.assume(report_from_db['ingredient'][0]._id == most_repeated_ingredient_id)
    pytest.assume(report_from_db['client_data'][0].client_name == most_repeated_client["client_name"])
    pytest.assume(report_from_db['client_data'][1].client_name == second_most_repeated_client["client_name"])
    pytest.assume(report_from_db['client_data'][2].client_name == third_most_repeated_client["client_name"])