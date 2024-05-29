import pytest
from unittest.mock import MagicMock
from workshop_pro.engines_subsystem import Engine
from workshop_pro.vehicles_subsystem.vehicle import Vehicle


class TestVehicle:
    def test_is_in_year(self):
        engine_mock = MagicMock(spec=Engine)
        vehicle = Vehicle(
            chassis="12345",
            price=20000,
            engine=engine_mock,
            model="Test Model",
            year=2020,
        )

        assert vehicle.is_in_year(2010, 2025) is True
        assert vehicle.is_in_year(2025, 2030) is False

    def test_is_in_speed(self):
        engine_mock = MagicMock(spec=Engine)
        engine_mock.is_in_speed.return_value = True
        vehicle = Vehicle(
            chassis="12345",
            price=20000,
            engine=engine_mock,
            model="Test Model",
            year=2020,
        )

        assert vehicle.is_in_speed(50, 100) is True
        engine_mock.is_in_speed.assert_called_once_with(50, 100)

    def test_is_in_price(self):
        engine_mock = MagicMock(spec=Engine)
        vehicle = Vehicle(
            chassis="12345",
            price=20000,
            engine=engine_mock,
            model="Test Model",
            year=2020,
        )

        assert vehicle.is_in_price(15000, 25000) is True
        assert vehicle.is_in_price(25000, 30000) is False

    def test_is_chassis(self):
        engine_mock = MagicMock(spec=Engine)
        vehicle = Vehicle(
            chassis="12345",
            price=20000,
            engine=engine_mock,
            model="Test Model",
            year=2020,
        )

        assert vehicle.is_chassis("12345") is True
        assert vehicle.is_chassis("54321") is False
