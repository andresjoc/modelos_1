""""
This module contains the Observer class

Author: Andres Acevedo

"""

from abc import abstractmethod


class Observer:
    """This class is an abstract class that represents an observer."""

    @abstractmethod
    def update(self, list_vehicles: list):
        """
        This method is used to update the observer.
        """

    def __str__(self):
        return "Observer"
