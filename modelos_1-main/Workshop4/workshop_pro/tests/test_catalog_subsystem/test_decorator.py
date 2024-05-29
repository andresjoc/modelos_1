"""
This module contains the tests for the Decorator class of the Catalog subsystem.

Author: Andres Jose Acevedo Avila <ajacevedoa@udidstrital.edu.co>
"""

import pytest
from unittest.mock import MagicMock
from workshop_pro.catalog_subsystem.decorator import (
    TimePerformanceDecorator,
    MemoryPerformanceDecoratorWindows,
    Catalog,
    Vehicle,
)


class TestTimePerformanceDecorator:

    @pytest.fixture
    def catalog_mock(self):
        mock = MagicMock(spec=Catalog)
        mock.get_all_vehicles.return_value = ["vehicle1", "vehicle2"]
        mock.get_by_speed.return_value = ["vehicle1"]
        mock.get_by_price.return_value = ["vehicle2"]
        return mock

    @pytest.fixture
    def decorator(self, catalog_mock):
        return TimePerformanceDecorator(catalog_mock)

    def test_get_all_vehicles(self, decorator, catalog_mock):
        result = decorator.get_all_vehicles()
        assert result == ["vehicle1", "vehicle2"]
        catalog_mock.get_all_vehicles.assert_called_once()

    def test_get_by_speed(self, decorator, catalog_mock):
        result = decorator.get_by_speed(10, 20)
        assert result == ["vehicle1"]
        catalog_mock.get_by_speed.assert_called_once_with(10, 20)

    def test_get_by_price(self, decorator, catalog_mock):
        result = decorator.get_by_price(1000, 2000)
        assert result == ["vehicle2"]
        catalog_mock.get_by_price.assert_called_once_with(1000, 2000)

    def test_add_vehicle(self, decorator, catalog_mock):
        decorator.add_vehicle("car")
        catalog_mock.add_vehicle.assert_called_once_with("car")

    def test_remove_vehicle(self, decorator, catalog_mock):
        vehicle = MagicMock(spec=Vehicle)
        decorator.remove_vehicle(vehicle)
        catalog_mock.remove_vehicle.assert_called_once_with(vehicle)


class TestMemoryPerformanceDecoratorWindows:
    """
    This class contains unit tests for the MemoryPerformanceDecoratorWindows class.
    """

    @pytest.fixture
    def catalog_mock(self):
        mock = MagicMock(spec=Catalog)
        mock.get_all_vehicles.return_value = ["vehicle1", "vehicle2"]
        mock.get_by_speed.return_value = ["vehicle1"]
        mock.get_by_price.return_value = ["vehicle2"]
        return mock

    @pytest.fixture
    def decorator(self, catalog_mock):
        return MemoryPerformanceDecoratorWindows(catalog_mock)

    def test_get_all_vehicles(self, decorator, catalog_mock):
        result = decorator.get_all_vehicles()
        assert result == ["vehicle1", "vehicle2"]
        catalog_mock.get_all_vehicles.assert_called_once()

    def test_get_by_speed(self, decorator, catalog_mock):
        result = decorator.get_by_speed(10, 20)
        assert result == ["vehicle1"]
        catalog_mock.get_by_speed.assert_called_once_with(10, 20)

    def test_get_by_price(self, decorator, catalog_mock):
        result = decorator.get_by_price(1000, 2000)
        assert result == ["vehicle2"]
        catalog_mock.get_by_price.assert_called_once_with(1000, 2000)

    def test_add_vehicle(self, decorator, catalog_mock):
        decorator.add_vehicle("car")
        catalog_mock.add_vehicle.assert_called_once_with("car")

    def test_remove_vehicle(self, decorator, catalog_mock):
        vehicle = MagicMock(spec=Vehicle)
        decorator.remove_vehicle(vehicle)
        catalog_mock.remove_vehicle.assert_called_once_with(vehicle)
