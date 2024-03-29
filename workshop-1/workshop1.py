# -*- coding: utf-8 -*-
"""Workshop1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1reHaJoCKR62WLYn7jIqnOwlF6U9w5jJf
"""

class Vehicle:
  """This class represent the structure of a vehicle"""
  def __init__(self, engine, model, gas_comsumption, year):

    self.engine = {
        "nombre": engine["nombre"],
        "tipo": engine["tipo"],
        "potencia": engine["potencia"],
        "peso": engine["peso"]
    }
    self.model = model
    self.gas_comsumption = gas_comsumption
    self.year = year


v_created = [] #Variables para vehiculos creados


class Car(Vehicle):
  """This is a class that represents a car"""
  def __init__(self, engine, model, gas_consumption, year):
    super().__init__(engine, model, gas_consumption, year)

class Truck(Vehicle):
  """This is a class that represents a Truck"""
  def __init__(self, engine, chasis, potency, weight):
    super().__init__(engine, model, gas_consumption, year)

class Yacht(Vehicle):
  """This is a class that represents a Yacht"""
  def __init__(self, engine, chasis, potency, weight):
    super().__init__(engine, model, gas_consumption, year)

class Motorcycle(Vehicle):
  """This is a class that represents a Motorcycle"""
  def __init__(self, engine, chasis, potency, weight):
    super().__init__(engine, model, gas_consumption, year)

def datos_basicos():
      engine_nombre = input("Ingrese el nombre del motor: ")
      engine_tipo = input("Ingrese el tipo de motor: ")
      engine_potencia = input("Ingrese la potencia del motor: ")
      engine_peso = input("Ingrese el peso del motor: ")

      engine = {
          "nombre": engine_nombre,
          "tipo": engine_tipo,
          "potencia": engine_potencia,
          "peso": engine_peso
      }

      model = input("Ingrese el modelo del vehículo: ")
      gas_consumption = input("Ingrese el consumo de gasolina del vehículo: ")
      year = input("Ingrese el año del vehículo")

      return engine, model, gas_consumption, year


message="""
Bienvenido al creador de vehículos
  Opción 1: Crear Carro
  Opción 2: Crear Camión
  Opción 3: Crear Yate
  Opción 4: Crear Moto
  Opción 5: Ver vehículos creados
  Opción 6: Buscar vehículo por año
  Opción 7: Salir
"""
while True:
  print(message)
  option = int(input("Elija una opción, escribiendo solamente el número de la opción"))

  if option == 1: #Car
    engine, model, gas_consumption, year = datos_basicos()
    car = Car(engine, model, gas_consumption, year)
    v_created.append(car)

    print("Carro creado exitosamente!")
    print(car.__dict__)

  elif option == 2: # Truck
        engine, model, gas_consumption, year = datos_basicos()  # Función para obtener datos específicos del camión
        truck = Truck(engine, model, gas_consumption, year)
        v_created.append(truck)

        print("Camión creado exitosamente!")
        print(truck.__dict__)

  elif option == 3: # Yacht
        engine, model, gas_consumption, year = datos_basicos()  # Función para obtener datos específicos del yate
        yacht = Yacht(engine, model, gas_consumption, year)
        v_created.append(yacht)

        print("Yate creado exitosamente!")
        print(yacht.__dict__)

  elif option == 4: # Motorcycle
        engine, model, gas_consumption, year = datos_basicos()  # Función para obtener datos específicos de la motocicleta
        motorcycle = Motorcycle(engine, model, gas_consumption, year)
        v_created.append(motorcycle)

        print("Motocicleta creada exitosamente!")
        print(motorcycle.__dict__)


  elif option == 5: #Created Vehicles
        print("Vehículos creados:")
        for vehiculo in v_created:
            print(vehiculo.__dict__)

  elif option == 6: #Find Vehicle by Year
    print()

  elif option == 7:
    print("Adios")
    break

  else:
    print("Seleccione una opción valida")
    print(message)
    option = int(input("Elija una opción, recuerdo escribir solamente el número de la opción"))