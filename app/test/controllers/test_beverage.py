import pytest
from app.controllers import BeverageController
from ..fixtures.beverages import beverage, beverages


def test_create_beverage(app, beverage: dict):
    created_beverage, error = BeverageController.create(beverage)
    assert error is None
    for param, value in beverage.items():
        assert param in created_beverage
        assert value == created_beverage[param]
    assert created_beverage['_id']


def test_update_beverage(app, beverage: dict):
    created_beverage, _ = BeverageController.create(beverage)
    updated_fields = {
        'name': 'updated',
        'price': 10
    }
    updated_beverage, error = BeverageController.update({
        '_id': created_beverage['_id'],
        **updated_fields
    })
    assert error is None
    beverage_from_database, error = BeverageController.get_by_id(created_beverage['_id'])
    assert error is None
    for param, value in updated_fields.items():
        assert updated_beverage[param] == value
        assert beverage_from_database[param] == value


def test_get_beverage_by_id(app, beverage: dict):
    created_beverage, _ = BeverageController.create(beverage)
    beverage_from_db, error = BeverageController.get_by_id(created_beverage['_id'])
    assert error is None
    for param, value in created_beverage.items():
        assert beverage_from_db[param] == value


def test_get_all_beverages(app, beverages: list):
    created_beverages = []
    for beverage in beverages:
        created_beverage, _ = BeverageController.create(beverage)
        created_beverages.append(created_beverage)

    beverages_from_db, error = BeverageController.get_all()
    searchable_beverages = {db_beverage['_id']: db_beverage for db_beverage in beverages_from_db}
    assert error is None
    for created_beverage in created_beverages:
        current_id = created_beverage['_id']
        assert current_id in searchable_beverages
        for param, value in created_beverage.items():
            assert searchable_beverages[current_id][param] == value
