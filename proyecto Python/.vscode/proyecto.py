# Base de datos (diccionario) para almacenar usuarios y sus contraseñas
usuarios_db = {}

def quitar_puntos_dni(dni):
    return dni.replace(".", "")

def guardar_base_de_datos():
    with open("base_de_datos.txt", "w") as archivo:
        for email, info in usuarios_db.items():
            dni_formateado = f"{info['dni'][:2]}.{info['dni'][2:5]}.{info['dni'][5:]}"
            usuario_str = f"{email},{info['nombre']},{info['apellido']},{dni_formateado},{info['edad']},{info['password']}\n"
            archivo.write(usuario_str)

def cargar_base_de_datos():
    try:
        with open("base_de_datos.txt", "r") as archivo:
            for linea in archivo:
                email, nombre, apellido, dni, edad, password = linea.strip().split(",")
                dni_sin_puntos = quitar_puntos_dni(dni)
                usuarios_db[email] = {"nombre": nombre, "apellido": apellido, "dni": dni_sin_puntos, "edad": int(edad), "password": password}
    except FileNotFoundError:
        pass

def registrar_usuario():
    print("Registro de nuevo usuario")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI (con o sin puntos, ej: 12.345.678): ")
    dni_sin_puntos = quitar_puntos_dni(dni)

    while True:
        edad = input("Edad: ")
        try:
            edad = int(edad)
            if edad < 0:
                raise ValueError
            break
        except ValueError:
            print("La edad debe ser un número entero positivo. Intente nuevamente.")

    email = input("Email: ")
    
    # Comprobacion de email ya está registrado
    if email in usuarios_db:
        print("El email ya está registrado.")
    else:
        # Registro del password
        while True:
            password = input("Registre su contraseña: ")
            password_confirm = input("Confirme su contraseña: ")
            if password == password_confirm:
                # Nuevo usuario para el diccionario
                usuarios_db[email] = {"nombre": nombre, "apellido": apellido, "dni": dni_sin_puntos, "edad": edad, "password": password}
                print("Usuario registrado exitosamente.")
                break
            else:
                print("Las contraseñas no coinciden. Intente nuevamente.")

def mostrar_usuarios():
    print("\nUsuarios registrados:")
    for email, info in usuarios_db.items():
        dni_formateado = f"{info['dni'][:2]}.{info['dni'][2:5]}.{info['dni'][5:]}"
        print(f"Email: {email}, Nombre: {info['nombre']}, Apellido: {info['apellido']}, DNI: {dni_formateado}, Edad: {info['edad']}")

def buscar_usuario():
    while True:
        print("\n--- Búsqueda de Usuario ---")
        print("1. Buscar por Email")
        print("2. Buscar por Nombre y Apellido")
        print("3. Buscar por DNI")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción (1/2/3/4): ")

        if opcion == "1":
            email = input("Ingrese el email del usuario que desea buscar: ")
            if email in usuarios_db:
                info = usuarios_db[email]
                print(f"Usuario encontrado:")
                print(f"Nombre: {info['nombre']}, Apellido: {info['apellido']}, Edad: {info['edad']}, DNI: {info['dni']}, Email: {email}")
            else:
                print("Usuario no encontrado.")
        elif opcion == "2":
            nombre = input("Ingrese el nombre del usuario: ")
            apellido = input("Ingrese el apellido del usuario: ")
            encontrado = False
            for email, info in usuarios_db.items():
                if info['nombre'].lower() == nombre.lower() and info['apellido'].lower() == apellido.lower():
                    print(f"Usuario encontrado:")
                    print(f"Nombre: {info['nombre']}, Apellido: {info['apellido']}, Edad: {info['edad']}, DNI: {info['dni']}, Email: {email}")
                    encontrado = True
            if not encontrado:
                print("Usuario no encontrado.")
        elif opcion == "3":
            dni_buscar = input("Ingrese el DNI del usuario que desea buscar: ")
            dni_buscar = quitar_puntos_dni(dni_buscar)
            encontrado = False
            for email, info in usuarios_db.items():
                if info['dni'] == dni_buscar:
                    print(f"Usuario encontrado:")
                    print(f"Nombre: {info['nombre']}, Apellido: {info['apellido']}, Edad: {info['edad']}, DNI: {info['dni']}, Email: {email}")
                    encontrado = True
            if not encontrado:
                print("Usuario no encontrado.")
        elif opcion == "4":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            
def login_usuario():
    print("\n--- Inicio de Sesión ---")
    email = input("Ingrese su email: ")
    password = input("Ingrese su contraseña: ")

    if email in usuarios_db and usuarios_db[email]["password"] == password:
        print("Inicio de sesión exitoso. ¡Bienvenido!")
    else:
        print("Credenciales incorrectas. Por favor, inténtelo nuevamente.")

def menu_principal():

    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar nuevo usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Buscar usuario")
        print("4. Iniciar sesión")
        print("5. Salir")

        opcion = input("Seleccione una opción: ") #Podria reemplazarlo por botones 

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            buscar_usuario()
        elif opcion == "4":
            login_usuario()
        elif opcion == "5":
            print("Saliendo del programa... ¡Adiós!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    cargar_base_de_datos()
    menu_principal()
    guardar_base_de_datos()
    
    
    
    
class Persona():
    
    def __init__(self , nombre , apellido, edad, dni):
        self.nombre = nombre