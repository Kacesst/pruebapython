	"tamano": "mediana",
	"precio": 15.67,
	"toppings": ["champinones", "pepperoni", "albahaca"],
	"queso_extra": false,
	"delivery": true,
	"cliente": {
		"nombre": "Jane Doe",
		"telefono": null,
		"correo": "janedoe@email.com"
  
  
  
  
  from cliente import Cliente
class Producto:
    def __init__(self, nombre, precio, descripcion, categoria, color, talle, stock, foto, materiales, diseño):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.categoria = categoria
        self.color = color
        self.talle = talle
        self.stock = stock
        self.foto = foto
        self.materiales = materiales
        self.diseño = diseño

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

    def actualizar_stock(self, cantidad):
        self.stock -= cantidad

    def mostrar_informacion(self):
        print(f"{self.nombre} - Categoría: {self.categoria} - Talle: {self.talle} - Color: {self.color}")
        print(f"Precio: ${self.precio} - Stock disponible: {self.stock}")
        print(f"Descripción: {self.descripcion}")

# Ejemplo de uso
producto1 = Producto("Camiseta", 25, "Camiseta de algodón", "Remeras", "Blanco", "M", 50, "foto_remera.jpg")
producto2 = Producto("Pantalón", 40, "Pantalón vaquero", "Pantalones", "Azul", "L", 30, "foto_pantalon.jpg")
producto3 = Producto("Zapatilla", 9, "Nike", "Zapatillas", "Air Force 1", "Virgil Abloh-designed", 30, "foto_zapatilla.jpg")

class Zapatilla(Producto):
    def __init__(self, nombre, precio, descripcion, categoria, color, talle, stock, marca, modelo):
        super().__init__(nombre, precio, descripcion, categoria, color, talle, stock)
        self.marca = marca
        self.modelo = modelo
        self.fotos = {}

    def agregar_foto(self, nombre_foto, url_foto):
        self.fotos[nombre_foto] = url_foto

    def mostrar_fotos(self):
        print(f"Fotos de {self.nombre}:")
        for nombre_foto, url_foto in self.fotos.items():
            print(f"{nombre_foto}: {url_foto}")

# Crear clientes
cliente1 = Cliente("Juan", "Pérez", "juan@example.com", "Calle 123", "12345678", "123456789", "contraseña123", "1234-5678-9101")
cliente2 = Cliente("María", "Gómez", "maria@example.com", "Avenida 456", "98765432", "987654321", "contraseña456", "0987-6543-2109")


# Agregar productos al carrito
cliente1.agregar_producto_al_carrito(producto1)
cliente1.agregar_producto_al_carrito(producto2)

cliente2.agregar_producto_al_carrito(producto2)
cliente2.agregar_producto_al_carrito(producto3)

# Mostrar el carrito de cada cliente
cliente1.mostrar_carrito()
cliente2.mostrar_carrito()










import json
from cliente import Cliente
from producto import Producto, Zapatilla

# Crear productos
remera1 = Producto("Remera Algodón", 25, "Remera cómoda y fresca", "Remeras", "Blanco", "M", 50, "foto_remera.jpg", "Algodón", "Estampado floral")
pantalon1 = Producto("Pantalón Vaquero", 40, "Pantalón cómodo y resistente", "Pantalones", "Azul", "L", 30, "foto_pantalon.jpg", "Denim", "Estilo recto")
zapatilla1 = Zapatilla("Zapatilla Nike", 70, "Zapatilla deportiva", "Zapatillas", "Blanco", "42", 20, "Nike", "Air Force 1")

# Cargar lista de productos
productos = [remera1, pantalon1, zapatilla1]

cliente1 = Cliente("Juan", "Pérez", "juan@example.com", "Calle 123", "12345678", "123456789", "contraseña123", "1234-5678-9101")
cliente1.agregar_producto_al_carrito(remera1, cantidad=2)
cliente1.agregar_producto_al_carrito(pantalon1, cantidad=1)

def mostrar_informacion_cliente(cliente):
    print("Información del cliente:")
    print(f"Nombre: {cliente.nombre} {cliente.apellido}")
    print(f"Correo: {cliente.correo}")
    print(f"Dirección: {cliente.direccion}")
    print(f"DNI: {cliente.dni}")
    print(f"Teléfono: {cliente.telefono}")
    print(f"Tarjeta de crédito: {cliente.tarjeta_credito}\n")

def mostrar_carrito_cliente(cliente):
    print("Carrito de", cliente.nombre, cliente.apellido + ":")
    for item in cliente.carrito:
        producto = item["producto"]
        cantidad = item["cantidad"]
        print(f"{producto.nombre} - Cantidad: {cantidad}")
    total_carrito = cliente.obtener_total_carrito()
    print(f"Total a pagar: ${total_carrito}\n")

def mostrar_galeria_productos(productos):
    print("======= GALERÍA DE PRODUCTOS =======")
    for idx, producto in enumerate(productos, 1):
        print(f"{idx}. {producto.nombre} - ${producto.precio}")
    print()

def agregar_producto_al_carrito(cliente, productos):
    mostrar_galeria_productos(productos)
    numero_producto = int(input("Ingrese el número de producto que desea agregar al carrito: "))
    producto_seleccionado = productos[numero_producto - 1]
    cantidad = int(input("Ingrese la cantidad que desea agregar al carrito: "))
    cliente.agregar_producto_al_carrito(producto_seleccionado, cantidad)
    print("Producto agregado al carrito.\n")

while True:
    print("======= MENÚ DE COMPRA =======")
    print("1. Ver información del cliente")
    print("2. Ver carrito")
    print("3. Ver galería de productos")
    print("4. Agregar producto al carrito")
    print("5. Salir")

    opcion = int(input("Ingrese el número de opción que desee: "))

    if opcion == 1:
        mostrar_informacion_cliente(cliente1)
    elif opcion == 2:
        mostrar_carrito_cliente(cliente1)
    elif opcion == 3:
        mostrar_galeria_productos(productos)
    elif opcion == 4:
        agregar_producto_al_carrito(cliente1, productos)
    elif opcion == 5:
        print("Gracias por utilizar nuestro servicio de compra. ¡Hasta pronto!")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número válido del menú.\n")

def agregar_producto_al_carrito(cliente, productos):
    while True:
        try:
            mostrar_galeria_productos(productos)
            numero_producto = int(input("Ingrese el número de producto que desea agregar al carrito: "))
            producto_seleccionado = productos[numero_producto - 1]
            cantidad = int(input("Ingrese la cantidad que desea agregar al carrito: "))
            cliente.agregar_producto_al_carrito(producto_seleccionado, cantidad)
            print("Producto agregado al carrito.\n")
            break
        except ValueError:
            print("Error: Ingrese un número válido de producto y cantidad.\n")
        except IndexError:
            print("Error: Ingrese un número de producto válido.\n")

def buscar_producto_por_nombre(nombre_producto, productos):
    for i, producto in enumerate(productos):
        if nombre_producto.lower() in producto.nombre.lower():
            return i
    return -1

def agregar_producto_al_carrito(cliente, productos):
    while True:
        try:
            mostrar_galeria_productos(productos)
            nombre_producto = input("Ingrese el nombre del producto que desea agregar al carrito: ")
            numero_producto = buscar_producto_por_nombre(nombre_producto, productos)
            if numero_producto == -1:
                raise ValueError
            producto_seleccionado = productos[numero_producto]
            cantidad = int(input("Ingrese la cantidad que desea agregar al carrito: "))
            cliente.agregar_producto_al_carrito(producto_seleccionado, cantidad)
            print("Producto agregado al carrito.\n")
            break
        except ValueError:
            print("Error: Producto no encontrado o cantidad inválida. Intente nuevamente.\n")

while True:
    try:
        print("======= MENÚ DE COMPRA =======")
        print("1. Ver información del cliente")
        print("2. Ver carrito")
        print("3. Ver galería de productos")
        print("4. Agregar producto al carrito")
        print("5. Salir")

        opcion = int(input("Ingrese el número de opción que desee: "))

        if opcion == 1:
            mostrar_informacion_cliente(cliente1)
        elif opcion == 2:
            mostrar_carrito_cliente(cliente1)
        elif opcion == 3:
            mostrar_galeria_productos(productos)
        elif opcion == 4:
            agregar_producto_al_carrito(cliente1, productos)
        elif opcion == 5:
            print("Gracias por utilizar nuestro servicio de compra. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido del menú.\n")
    except ValueError:
        print("Error: Ingrese un número válido de opción.\n")
        
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

# Función para registrar un nuevo usuario
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

# Resto del código (menu_usuarios, login_usuario, mostrar_usuarios, buscar_usuario, menu_principal)

if __name__ == "__main__":
    cargar_base_de_datos()
    menu_principal()
    
    
    
    
    
    
    agregar_producto_al_carrito(cliente1, productos)
    elif opcion == :
        
        
        
        
        
        