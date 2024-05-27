class User:
    def __init__(self, username, password, user_type):
        self.username = username
        self.password = password
        self.user_type = user_type  # Puede ser 'Admin' o 'User'

# Definir usuarios pre-registrados
admin_user = User("admin", "admin_password", "Admin")
regular_user = User("user", "user_password", "User")

class AuthenticationSystem:
    def __init__(self):
        pass  # Aquí podrías agregar lógica adicional si fuera necesario

    def authenticate_user(self, username, password):
        if username == admin_user.username and password == admin_user.password:
            return admin_user.user_type
        elif username == regular_user.username and password == regular_user.password:
            return regular_user.user_type
        else:
            return None

class VehicleManagementSystem:
    def __init__(self, auth_system):
        self.auth_system = auth_system
        self.catalog = Catalog()

    def add_vehicle(self, user, vehicle):
        if user == 'Admin':
            self.catalog.add_vehicle(vehicle)
            print("Vehículo agregado al catálogo con éxito!")
        else:
            print("¡No estás autorizado para realizar esta acción!")

    # Otras funciones para actualizar y eliminar vehículos

if __name__ == "__main__":
    auth_system = AuthenticationSystem()
    vehicle_management_system = VehicleManagementSystem(auth_system)

    # Iniciar sesión
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    user_type = auth_system.authenticate_user(username, password)

    if user_type:
        print(f"Bienvenido, {username}!")
        if user_type == 'Admin':
            # Mostrar opciones para administradores
            print("Opciones disponibles para administradores:")
            # Aquí puedes llamar a las funciones para agregar, actualizar y eliminar vehículos
        else:
            # Mostrar opciones para usuarios regulares
            print("Opciones disponibles para usuarios regulares:")
            # Aquí puedes llamar a las funciones para ver y buscar vehículos
    else:
        print("Nombre de usuario o contraseña incorrectos.")

