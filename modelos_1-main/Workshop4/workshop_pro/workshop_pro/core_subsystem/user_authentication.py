"""
This module has some classes related to users and authentication.

Author: Carlos Andrés Sierra <cavirguezs@udistrital.edu.co>
"""

import json
from ..newsletter_subsystem import Observer


# pylint: disable=attribute-defined-outside-init
class User(Observer):
    """This is a data class to represents the User information."""

    def __init__(self, username: str, grants: dict, email: str):
        self.__username = username
        self.__grants = grants
        self.__email = email

    def get_username(self):
        """This method returns the username."""
        return self.__username

    def get_email(self):
        """This method returns the email."""
        return self.__email

    def is_grant(self, grant: str):
        """This method returns if the user has a grant."""
        return self.__grants[grant]

    def update(self, list_vehicles: list):
        print("Mira este es nuestro catálogo: ")
        for vehicle in list_vehicles:
            print(vehicle)


class Authentication:
    """This class is used to validate users authentication."""

    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password
        self.__grants = None

    def authenticate(self) -> bool:
        """This method validates the user credentials."""
        with open("users.json", "r", encoding="UTF-8") as file:
            users = json.load(file)
        for user in users:
            if (
                user["username"] == self.__username
                and user["password"] == self.__password
            ):
                self.__email = user["email"]
                self.__grants = user["grants"]
                return True
        return False

    def userdata(self) -> User:
        """This method returns the user data."""
        return User(self.__username, self.__grants, self.__email)
