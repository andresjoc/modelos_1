"""
This file contains a Catalog class and an entry poiny menu
for vehicles catalog application.
"""

from typing import List

from vehicles import Vehicle

class Catalog:
    """
    A class representing a catalog of vehicles.
    """

    def __init__(self):
        """
        Initializes a new instance of the Catalog class.
        """
        self.__vehicles = []

    def __new__(cls):
        """
        Creates a new instance of the Catalog class if it doesn't already exist.
        """
        if not hasattr(cls, "instance"):
            cls.instance = super(Catalog, cls).__new__(cls)
            cls.instance.vehicles = []
        return cls.instance

    def get_all_vehicles(self) -> List[Vehicle]:
        """
        Returns a list of all vehicles in the catalog.
        
        Returns:
            A list of Vehicle objects.
        """
        return self.__vehicles

    def get_price_by_range(self, min_price: float, max_price: float) -> List[Vehicle]:
        """
        Returns a list of vehicles within the specified price range.
        
        Args:
            min_price: The minimum price of the vehicles.
            max_price: The maximum price of the vehicles.
        
        Returns:
            A list of Vehicle objects within the specified price range.
        """
        return [vehicle for vehicle in self.__vehicles if min_price <= vehicle.price <= max_price]

    def add_vehicle(self, vehicle: Vehicle):
        """
        Adds a vehicle to the catalog.
        
        Args:
            vehicle: The Vehicle object to be added.
        """
        self.__vehicles.append(vehicle)
