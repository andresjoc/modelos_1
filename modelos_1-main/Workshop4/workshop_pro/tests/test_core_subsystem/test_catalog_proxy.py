import pytest
from unittest.mock import MagicMock, patch
from workshop_pro.core_subsystem.catalog_proxy import (
    CatalogProxy,
    Catalog,
    Observability,
)


class TestCatalogProxy:

    @pytest.fixture
    def catalog_mock(self):
        return MagicMock(spec=Catalog)

    @pytest.fixture
    def catalog_proxy(self, catalog_mock):
        with patch(
            "workshop_pro.core_subsystem.catalog_proxy.Catalog",
            return_value=catalog_mock,
        ):
            with patch(
                "workshop_pro.core_subsystem.catalog_proxy.TimeDecorator",
                return_value=catalog_mock,
            ):
                with patch(
                    "workshop_pro.core_subsystem.catalog_proxy.MemoryDecorator",
                    return_value=catalog_mock,
                ):
                    return CatalogProxy()

    def test_add_vehicle(self, catalog_proxy, catalog_mock):
        with patch("builtins.input", return_value="Car"):
            with patch.object(Observability, "write_user_log") as mock_write_user_log:
                catalog_proxy.add_vehicle("test_user")
                catalog_mock.add_vehicle.assert_called_once_with("Car")
                mock_write_user_log.assert_called_once_with(
                    "test_user", "A new vehicle had been added."
                )

    def test_remove_vehicle(self, catalog_proxy, catalog_mock):
        with patch("builtins.input", return_value="123"):
            catalog_proxy.remove_vehicle()
            catalog_mock.remove_vehicle.assert_called_once_with("123")

    def test_get_all_vehicles(self, catalog_proxy, catalog_mock):
        catalog_mock.get_all_vehicles.return_value = ["Vehicle1", "Vehicle2"]
        with patch("builtins.print") as mock_print:
            catalog_proxy.get_all_vehicles()
            mock_print.assert_any_call("Vehicle1")
            mock_print.assert_any_call("Vehicle2")

    def test_get_vehicles_by_speed(self, catalog_proxy, catalog_mock):
        catalog_mock.get_by_speed.return_value = ["Vehicle1"]
        with patch("builtins.input", side_effect=["10", "20"]):
            with patch("builtins.print") as mock_print:
                catalog_proxy.get_vehicles_by_speed()
                catalog_mock.get_by_speed.assert_called_once_with("10", "20")
                mock_print.assert_any_call("Vehicle1")

    def test_get_vehicles_by_price(self, catalog_proxy, catalog_mock):
        catalog_mock.get_by_price.return_value = ["Vehicle2"]
        with patch("builtins.input", side_effect=["1000", "2000"]):
            with patch("builtins.print") as mock_print:
                catalog_proxy.get_vehicles_by_price()
                catalog_mock.get_by_price.assert_called_once_with("1000", "2000")
                mock_print.assert_any_call("Vehicle2")
