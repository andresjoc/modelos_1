"""
This module contains the Newsletter class that is responsible for sending newsletters.

Author: Andres Jose Acevedo Avila

"""

from ..core_subsystem import FinalCatalog


class Newsletter:
    """This class is responsible for sending newsletters."""

    def __init__(self):
        self.__subscribers = []
        self.__catalog = FinalCatalog().get_list_of_vehicles()

    def add_subscriber(self, subscriber):
        """
        This method is used to add a subscriber to the newsletter.
        """
        self.__subscribers.append(subscriber)
        print("Subscriber added successfully!")

    def remove_subscriber(self, subscriber):
        """
        This method is used to remove a subscriber from the newsletter.
        """
        self.__subscribers.remove(subscriber)
        print("Subscriber removed successfully!")

    def notify_subscribers(self):
        """
        This method is used to notify the subscribers of the newsletter.
        """
        print(self.__catalog)
        if len(list(self.__catalog)) > 5:
            # Devuelve los últimos 5 elementos de la lista vehículos
            for subscriber in self.__subscribers:
                subscriber.update(list(self.__catalog)[-5:])
        elif len(list(self.__catalog)) == 0:
            print("There are no vehicles in the catalog.")
        else:
            for subscriber in self.__subscribers:
                subscriber.update(list(self.__catalog))
