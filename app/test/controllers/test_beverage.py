import pytest
from app.controllers import BeverageController


def test_create_beverage_when_function_have_a_dict_should_return_a_created_beverage(
    app, beverage: dict
):
    created_beverage, error = BeverageController.create(entry=beverage)
    pytest.assume(error is None)
    for param, value in beverage.items():
        pytest.assume(param in created_beverage)
        pytest.assume(value == created_beverage[param])
        pytest.assume(created_beverage["_id"])


def test_update_beverage_when_function_have_a_dict_should_return_a_updated_beverage(
    app, beverage: dict
):
    created_beverage, _ = BeverageController.create(entry=beverage)
    updated_fields = {"name": "updated", "price": 10}
    updated_beverage, error = BeverageController.update(
        new_values={"_id": created_beverage["_id"], **updated_fields}
    )
    pytest.assume(error is None)
    beverage_from_database, error = BeverageController.get_by_id(
        _id=created_beverage["_id"]
    )
    pytest.assume(error is None)
    for param, value in updated_fields.items():
        pytest.assume(updated_beverage[param] == value)
        pytest.assume(beverage_from_database[param] == value)


def test_get_beverage_by_id_when_function_have_a_dict_should_return_a_beverage(
    app, beverage: dict
):
    created_beverage, _ = BeverageController.create(entry=beverage)
    beverage_from_db, error = BeverageController.get_by_id(_id=created_beverage["_id"])
    pytest.assume(error is None)
    for param, value in created_beverage.items():
        pytest.assume(beverage_from_db[param] == value)


def test_get_all_beverages_when_function_have_a_dict_should_return_all_beverages(
    app, beverages: list
):
    created_beverages = []
    for beverage in beverages:
        created_beverage, _ = BeverageController.create(entry=beverage)
        created_beverages.append(created_beverage)

    beverages_from_db, error = BeverageController.get_all()
    searchable_beverages = {
        db_beverage["_id"]: db_beverage for db_beverage in beverages_from_db
    }
    pytest.assume(error is None)
    for created_beverage in created_beverages:
        current_id = created_beverage["_id"]
        assert current_id in searchable_beverages
        for param, value in created_beverage.items():
            pytest.assume(searchable_beverages[current_id][param] == value)
