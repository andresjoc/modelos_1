"""
This file has a set of classes related to vehicles,
including of the all subtypes of vehicles.


Author: Carlos Sierra - cavirguez@udistrital.edu.co
"""

from engines import Engine

class VehicleFlyweight:
    """This class is a flyweight to create vehicle objects"""

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"Vehicle: color={self.color}"
    

# pylint: disable=too-few-public-methods
class Vehicle:
    """This class represents an abstraction of a vehicle inside the catalog business model."""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        flyweight,
        engine: Engine,
        chassis: str,
        price: float,
        model: str,
        year: int,
        consumption: float,
    ):
        self.flyweight = flyweight        
        self.engine = engine
        self.chassis = chassis
        self.price = price
        self.model = model
        self.year = year
        self.consumption = consumption

    def __str__(self):
        return (
            f"Modelo: {self.model}\n"
            f"Año: {self.year}\n"
            f"Precio: ${self.price}\n"
            f"Consumo: {self.consumption} km/l\n"
            f"Motor: {self.engine}\n"
            f"Chasis: {self.chassis}\n"
        )


class FlyweightFactory:
    """
    Flyweight factory that stores and provides instances of Flyweight.
    
    """
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, color):
        """
            It gets a Flyweight instance if it already exists, or creates and stores it if it doesn't exist.
        """
        key = f"{color}"
        if key not in self.flyweights:
            self.flyweights[key] = VehicleFlyweight(color)
        return self.flyweights[key]





class Helicopter(Vehicle):
    """This class is a concrete implementation of an helicopter"""


class Scooter(Vehicle):
    """This class is a concrete implementation of a scoorter"""


class Motorcycle(Vehicle):
    """This class is a concrete implementation of a motorcycle"""


class Car(Vehicle):
    """This class is a concrete implementation of a car"""

    def __init__(
        self,
        flyweight,
        engine: Engine,
        chassis: str,
        price: float,
        model: str,
        year: int,
        consumption: float,
        transmission: str,
        trade: str,
        combustible_type: str,
    ):
        super().__init__(flyweight, engine, chassis, price, model, year, consumption)
        self.transmission = transmission
        self.trade = trade
        self.combustible_type = combustible_type


class Truck(Vehicle):
    """This class is a concrete implemtantion of a truck"""

    def calculate_gas_consupmtion(self) -> float:
        """
        This method calculates consumption based on engine
        values.

        Returns:
        - float: vehicle consumption
        """
        consumption = (
            (1.1 * self.engine.power)
            + (0.2 * self.engine.weight)
            + (0.3 if self.chassis == "A" else 0.5)
        )
        return consumption


class Yacht(Vehicle):
    """This class is a concrete implementation of a yatch"""

    def __init__(
        self,
        flyweight,
        engine: Engine,
        chassis: str,
        price: float,
        model: str,
        year: int,
        consumption: float,
        length: float,
        weight: float,
        trade: str,
    ):
        super().__init__(flyweight, engine, chassis, price, model, year, consumption)
        self.length = length
        self.weight = weight
        self.trade = trade
