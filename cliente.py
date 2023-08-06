import json
from producto import Producto


class Cliente:
    def __init__(self, nombre, apellido, correo, direccion, dni, telefono, contraseña, tarjeta_credito):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.direccion = direccion
        self.dni = dni
        self.telefono = telefono
        self.contraseña = contraseña
        self.tarjeta_credito = tarjeta_credito
        self.carrito = []
        
        
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
                
    def login_usuario():
        print("\n--- Inicio de Sesión ---")
        email = input("Ingrese su email: ")
        password = input("Ingrese su contraseña: ")

    if email in usuarios_db and usuarios_db[email]["password"] == password:
        print("Inicio de sesión exitoso. ¡Bienvenido!")
    else:
        print("Credenciales incorrectas. Por favor, inténtelo nuevamente.")

    
    def guardar_cliente_json(self):
        data = {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "correo": self.correo,
            "direccion": self.direccion,
            "dni": self.dni,
            "telefono": self.telefono,
            "contraseña": self.contraseña,
            "tarjeta_credito": self.tarjeta_credito,
            "carrito": [item["producto"].to_json() for item in self.carrito]
        }

        with open(f"{self.nombre}_{self.apellido}.json", "w") as archivo_json:
            json.dump(data, archivo_json)
            
            
    @classmethod
    def cargar_cliente_desde_json(cls, nombre, apellido):
                with open(f"{nombre}_{apellido}.json", "r") as archivo_json:
                    datos_cliente = json.load(archivo_json)

                cliente = cls(
                    datos_cliente["nombre"],
                    datos_cliente["apellido"],
                    datos_cliente["correo"],
                    datos_cliente["direccion"],
                    datos_cliente["dni"],
                    datos_cliente["telefono"],
                    datos_cliente["contraseña"],
                    datos_cliente["tarjeta_credito"]
                )

                # Agregar productos al carrito
                for item in datos_cliente["carrito"]:
                    producto = Producto(
                        item["nombre"],
                        item["precio"],
                        item["descripcion"],
                        item["categoria"],
                        item["color"],
                        item["talle"],
                        item["stock"],
                        item["foto"],
                        item["materiales"],
                        item["diseño"]
                    )
                    cliente.agregar_producto_al_carrito(producto, cantidad=item["cantidad"])

                return cliente
    def guardar_cliente_json(self):
        with open(f"{self.nombre}_{self.apellido}.json", "w") as archivo_json:
            # Convertir el carrito a una lista de diccionarios con la cantidad de cada producto
            carrito_serializado = []
            for item in self.carrito:
                producto_dict = item["producto"].__dict__
                producto_dict["cantidad"] = item["cantidad"]
                carrito_serializado.append(producto_dict)

            # Agregar el carrito serializado al diccionario del cliente
            self.__dict__["carrito"] = carrito_serializado

            # Guardar el cliente en el archivo JSON
            json.dump(self.__dict__, archivo_json)