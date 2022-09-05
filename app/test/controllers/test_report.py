import pytest

from app.controllers.order import OrderController


def test_get_all(app, create_repeted_clients_and_ingredients_order):

    orders, most_repeated_client, most_repeated_ingredient = create_repeted_clients_and_ingredients_order
    for order in orders:
        created_order, error = OrderController.create(order)
        pytest.assume(error is None)
    report_from_db, error = ReportController.get()
    pytest.assume(error is None)
    
    for param, value in report_from_db.items():
        pytest.assume(param['ingredient'])
        pytest.assume(param['client_data'])
        pytest.value(param['ingredient'].get("name") == most_repeated_ingredient["name"])
        pytest.value(param['client_data'][1] in most_repeated_client)