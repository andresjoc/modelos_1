from catalog import Catalog
from factories import HighEngineFactory, PoorEngineFactory
from vehicles import *


class Facade:
    """
    The Facade class provides a simplified interface for interacting with the catalog of vehicles.
    It encapsulates the complex logic and interactions between different classes.
    """

    def __init__(self):
        self.catalog = Catalog()
        self.cache = []

    def menu(self):
        """
        Displays a menu to the user and handles the user's input for adding a vehicle to the catalog.
        """

        # Solicitar al usuario el tipo de vehículo que desea agregar
        print("Seleccione el tipo de vehículo que desea agregar:")
        print("1. Automóvil")
        print("2. Motocicleta")
        print("3. Scooter")
        print("4. Camión")
        print("5. Yate")
        vehicle_type = int(input("Opción: "))

        # Solicitar al usuario los detalles del vehículo
        model = input("Ingrese el modelo del vehículo: ")
        year = int(input("Ingrese el año del vehículo: "))
        price = float(input("Ingrese el precio del vehículo: "))
        comsumption = float(input("Ingrese el consumo del vehículo: "))
        chassis = input("Ingrese el chasis del vehículo: ")

        color = input("Ingrese el color del vehículo: ")

        # Obtener una instancia del Flyweight correspondiente al color
        flyweight_factory = FlyweightFactory()
        flyweight = flyweight_factory.get_flyweight(color)

        # Crear una fábrica de motores según la selección del usuario
        print("Seleccione el tipo de motor:")
        print("1. Motor de alta calidad")
        print("2. Motor económico")
        engine_type = int(input("Opción: "))

        if engine_type == 1:
            engine_factory = HighEngineFactory()
        else:
            engine_factory = PoorEngineFactory()

        # Crear el motor del vehículo
        engine = engine_factory.create_electric_engine() if vehicle_type != 5 else engine_factory.create_gas_engine()

        # Crear el vehículo según la selección del usuario
        if vehicle_type == 1:
            transmission = input("Ingrese el tipo de transmisión del automóvil: ")
            trade = input("Ingrese el comerciante del automóvil: ")
            combustible_type = input("Ingrese el tipo de combustible del automóvil: ")
            vehicle = Car(flyweight, engine, chassis, price, model, year, comsumption, transmission, trade, combustible_type)
        elif vehicle_type == 2:
            vehicle = Motorcycle(flyweight, engine, chassis, price, model, year, comsumption)
        elif vehicle_type == 3:
            vehicle = Scooter(flyweight, engine, chassis, price, model, year, comsumption)
        elif vehicle_type == 4:
            vehicle = Truck(flyweight, engine, chassis, price, model, year, comsumption)
        elif vehicle_type == 5:
            length = float(input("Ingrese la longitud del yate: "))
            weight = float(input("Ingrese el peso del yate: "))
            trade = input("Ingrese el comerciante del yate: ")
            vehicle = Yacht(flyweight, engine, chassis, price, model, year, comsumption, length, weight, trade)

        # Agregar el vehículo al catálogo
        self.catalog.add_vehicle(vehicle)
        print("¡Vehículo agregado al catálogo con éxito!")

    def search_vehicle_by_price(self):
        """
        Prompts the user to enter a price range and searches for vehicles within that range in the catalog.
        Displays the found vehicles and adds them to the cache.
        """

        # Solicitar al usuario el rango de precios
        min_price = float(input("Ingrese el precio mínimo: "))
        max_price = float(input("Ingrese el precio máximo: "))

        # Buscar vehículos en el catálogo por rango de precios
        vehicles = self.catalog.get_price_by_range(min_price, max_price)

        # Mostrar los vehículos encontrados
        if vehicles:
            print("\nVehículos encontrados en el rango de precios:")
            for vehicle in vehicles:
                print(vehicle)
                self.add_vehicle_to_cache(vehicle)  # Add searched vehicle to cache
        else:
            print("No se encontraron vehículos en el rango de precios especificado.")

    def add_vehicle_to_cache(self, vehicle):
        """
        Adds a vehicle to the cache. If the cache is full, removes the oldest entry before adding the new vehicle.
        """

        if len(self.cache) >= 5:
            self.cache.pop(0)  # Borrar la entrada más vieja
        self.cache.append(vehicle)

    def view_cache(self):
        """
        Displays the last 5 vehicles searched by the user.
        """

        if self.cache:
            print("\nÚltimos 5 vehículos buscados:")
            for index, vehicle in enumerate(self.cache, start=1):
                print(f"{index}. {vehicle}")
        else:
            print("La caché está vacía.")

    def clear_cache(self):
        """
        Clears the cache of searched vehicles.
        """

        self.cache.clear()
        print("La caché ha sido borrada.")

    def run(self):
        """
        Runs the main console interface for managing the catalog of vehicles.
        """

        while True:
            print("\nBienvenido al sistema de gestión de catálogos de vehículos")
            print("1. Agregar vehículo al catálogo")
            print("2. Buscar vehículos por rango de precios")
            print("3. Ver caché de vehículos buscados")
            print("4. Borrar caché de vehículos buscados")
            print("5. Salir")
            option = int(input("Seleccione una opción: "))

            if option == 1:
                self.menu()
            elif option == 2:
                self.search_vehicle_by_price()
            elif option == 3:
                self.view_cache()
            elif option == 4:
                self.clear_cache()
            elif option == 5:
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione nuevamente.")

if __name__ == "__main__":
    facade = Facade()
    facade.run()