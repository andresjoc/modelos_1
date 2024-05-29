"""
This files has some tests for the CatalogConcrete class.

Author: Andres Acevedo <ajacevedoa@udistrital.edu.co>
"""

from workshop_pro.catalog_subsystem.catalog import CatalogConcrete


class TestCatalogConcrete:
    """This class tests the CatalogConcrete class"""

    def setup_method(self):
        self.catalog = CatalogConcrete()

    def test_get_all_vehicles(self):
        """This is a simple test case to verify the creation of a catalog with no vehicles."""
        assert len(self.catalog.get_all_vehicles()) == 0

    def test_get_by_speed(self):
        """This is a simple test case to verify the creation of a catalog by speed with no vehicles."""
        assert len(self.catalog.get_by_speed(0, 100000000)) == 0

    def test_get_by_price(self):
        """This is a simple test case to verify the creation of a catalog by price with no vehicles."""
        assert len(self.catalog.get_by_price(0, 100000000)) == 0
