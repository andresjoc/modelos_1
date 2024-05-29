"""
This module has a singleton implementation of a catalog including the 
addition of decorators.

Author: Carlos Andrés Sierra <cavirguezs@udistrital.edu.co>
"""

from ..catalog_subsystem import Catalog, TimeDecorator, MemoryDecorator
from ..observability_subsystem import Observability


class CatalogProxy:
    """This class is a proxy for the catalog class."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CatalogProxy, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.__catalog = Catalog()
        self.__catalog = TimeDecorator(self.__catalog)
        self.__catalog = MemoryDecorator(self.__catalog)
        self.__backup = None
        self.cache = None

    def add_vehicle(self, username: str):
        """
        This method adds a vehicle to the catalog.

        Args:
            username (str): The username of the user who is adding the vehicle.
        """
        print(
            "Vehicle Types:\n\
            1. Car\n\
            2. Motorcycle\n\
            3. Truck\n\
            4. Yacht\n\
            5. Scooter\n\
            6. Helicopter\n"
        )
        vehicle_type = input("Vehicle type: ")
        self.__catalog.add_vehicle(vehicle_type)

        Observability.write_user_log(username, "A new vehicle had been added.")

    def remove_vehicle(self):
        """This method removes a vehicle from the catalog."""
        vehicle_id = input("Write the ID of the vehicle to remove")
        self.__backup = self.__catalog
        self.__catalog.remove_vehicle(vehicle_id)

    def get_all_vehicles(self):
        """This method gets all vehicles from the catalog."""
        for vehicle in self.__catalog.get_all_vehicles():
            print(str(vehicle))

    def get_vehicles_by_speed(self):
        """This method gets vehicles by speed from the catalog."""
        min_speed = input("Minimum speed: ")
        max_speed = input("Maximum speed: ")
        for vehicle in self.__catalog.get_by_speed(min_speed, max_speed):
            print(str(vehicle))
        self.cache = self.__catalog.get_by_speed(min_speed, max_speed)[-3:]

    def get_vehicles_by_price(self):
        """This method gets vehicles by price from the catalog."""
        min_price = input("Minimum price: ")
        max_price = input("Maximum price: ")
        for vehicle in self.__catalog.get_by_price(min_price, max_price):
            print(str(vehicle))
        self.cache = self.__catalog.get_by_price(min_price, max_price)[-3:]

    def get_list_of_vehicles(self):
        """This method gets a list of vehicles from the catalog."""
        self.cache = self.__catalog.get_all_vehicles()[-3:]
        return self.__catalog.get_all_vehicles()

    def undo_remove(self):
        """This method undoes the last remove operation."""
        self.__catalog = self.__backup
        self.__backup = self.__catalog
        print("The last remove operation has been undone.")

    def get_cache(self):
        """This method returns the cache."""
        return self.cache
