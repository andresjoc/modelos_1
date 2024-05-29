"""
This is the main file of the project. It is the entry point of the application.

Author: Carlos Andrés Sierra <cavirguezs@udistrital.edu.co>
"""

from .newsletter_subsystem import Newsletter
from .core_subsystem import FinalCatalog, Authentication

CATALOG = FinalCatalog()
NEWSLETTER = Newsletter()
MENU_OPTIONS = """
0. Log in the system
1. Add a new vehicle
2. Remove a vehicle
3. Search all vehicles
4. Search vehicles by speed
5. Search vehicles by price
6. Add subscriber to the newsletter
7. Remove subscriber from the newsletter
8. Notify subscribers
9. Undo Remove
10. Watch the last searches
11. Exit
"""


def login():
    """This function allows the user to log in the system."""
    username = input("Username: ")
    password = input("Password: ")

    auth = Authentication(username, password)

    if auth.authenticate():
        return auth.userdata()
    return None


# pylint: disable=too-many-branches
# pylint: disable=too-many-statements
def main():
    """This if the main file of the project."""
    user = None

    print("Welcome to the Vehicle Catalog System")
    print(MENU_OPTIONS)

    while True:
        option = input("Please select an option: ")

        if option == "0":
            print("====== Logging in the system ======")
            user = login()
        elif option == "1":
            print("====== Adding a new vehicle ======")
            if user.is_grant("add_vehicle"):
                print(user.get_username())
                CATALOG.add_vehicle(user.get_username())
        elif option == "2":
            print("====== Removing a vehicle ======")
            if user.is_grant("remove_vehicle"):
                CATALOG.remove_vehicle()
        elif option == "3":
            print("====== Searching all vehicles ======")
            if user.is_grant("search_vehicle"):
                CATALOG.get_all_vehicles()
        elif option == "4":
            print("====== Searching vehicles by speed ======")
            if user.is_grant("search_vehicle"):
                CATALOG.get_vehicles_by_speed()
        elif option == "5":
            print("====== Searching vehicles by price ======")
            if user.is_grant("search_vehicle"):
                CATALOG.get_vehicles_by_price()
        elif option == "6":
            print("====== Adding subscriber to the newsletter ======")
            if user.is_grant("add_subscriber"):
                NEWSLETTER.add_subscriber(user.get_email())
        elif option == "7":
            print("====== Removing subscriber from the newsletter ======")
            if user.is_grant("remove_subscriber"):
                NEWSLETTER.remove_subscriber(user.get_email())
        elif option == "8":
            print("====== Notifying subscribers ======")
            if user.is_grant("notify_subscriber"):
                NEWSLETTER.notify_subscribers()
        elif option == "9":
            print("====== Undo Remove ======")
            if user.is_grant("undo_remove"):
                CATALOG.undo_remove()
        elif option == "10":
            print("Watch the last searches")
            if user.is_grant("watch_cache"):
                if FinalCatalog().get_cache().equals([]):
                    print("No searches have been made yet.")
                else:
                    print("The searches are: ", FinalCatalog().get_cache())
        elif option == "11":
            print("Exiting the system.")
            break
        else:
            print("Invalid option. Please select a valid option.")

        print("\n" + MENU_OPTIONS + "\n\n")

    print("Thank you for using the Vehicle Catalog System.")


if __name__ == "__main__":
    main()
