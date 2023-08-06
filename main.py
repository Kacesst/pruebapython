import json
from cliente import Cliente, registrar_usuario
from producto import Producto, Zapatilla
from carrito import Carrito

remera1 = Producto("Remera Algodón", 25, "Remera cómoda y fresca", "Remeras", "Blanco", "M", 50, "foto_remera.jpg", "Algodón", "Estampado floral", "Colaboración X")
pantalon1 = Producto("Pantalón Vaquero", 40, "Pantalón cómodo y resistente", "Pantalones", "Azul", "L", 30, "foto_pantalon.jpg", "Denim", "Estilo recto", "Colaboración Y")
zapatilla1 = Zapatilla("Zapatilla Nike", 70, "Zapatilla deportiva", "Zapatillas", "Blanco", "42", 20, "foto_zapatilla1.jpg", "Nike", "Air Force 1", "Colaboración Z")
zapatilla2 = Zapatilla("Adidas Superstar", 80, "Zapatilla clásica de Adidas", "Zapatillas", "Negro", "41", 15, "foto_zapatilla2.jpg", "Adidas", "Superstar", "Sin colaboración")
zapatilla3 = Zapatilla("Converse Chuck Taylor", 60, "Zapatilla emblemática de Converse", "Zapatillas", "Rojo", "39", 12, "foto_zapatilla3.jpg", "Converse", "Chuck Taylor", "Colaboración W")
gorra1 = Producto("Gorra New York Yankees", 30, "Gorra oficial del equipo New York Yankees", "Gorras", "Negro", "Talla única", 20, "foto_gorra1.jpg", "Algodón", "Estilo 1", "Sin colaboración")
gorra2 = Producto("Gorra Los Angeles Dodgers", 25, "Gorra oficial del equipo Los Angeles Dodgers", "Gorras", "Azul", "Talla única", 18, "foto_gorra2.jpg", "Algodón", "Estilo 2", "Colaboración V")

# Cargar lista de productos
productos = [remera1, pantalon1, zapatilla1, zapatilla2, zapatilla3, gorra1, gorra2]

cliente1 = Cliente("Juan", "Pérez", "juan@example.com", "Calle 123", "12345678", "123456789", "contraseña123", "1234-5678-9101")


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
    while True:
        nombre_producto = input("Ingrese el nombre del producto que desea agregar al carrito: ")
        numero_producto = buscar_producto_por_nombre(nombre_producto, productos)
        if numero_producto == -1:
            print("Error: Producto no encontrado. Intente nuevamente.")
        else:
            producto_seleccionado = productos[numero_producto]
            break
    return producto_seleccionado

def agregar_producto_al_carrito(cliente, productos):
    while True:
        try:
            mostrar_galeria_productos(productos)
            numero_producto = int(input("Ingrese el número de producto que desea agregar al carrito: "))
            producto_seleccionado = productos[numero_producto - 1]
            cantidad = int(input("Ingrese la cantidad que desea agregar al carrito: "))
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser un número entero positivo.")
            cliente.agregar_producto_al_carrito(producto_seleccionado, cantidad)
            print("Producto agregado al carrito.\n")
            break
        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.\n")
        except IndexError:
            print("Error: Ingrese un número de producto válido.\n")
            
    # Función para buscar un producto por su nombre en la lista de productos
def buscar_producto_por_nombre(nombre_producto, productos):
    for i, producto in enumerate(productos):
        if nombre_producto.lower() in producto.nombre.lower():
            return i
    return -1

def menu_inicio():
    while True:
        print("======= MENÚ DE INICIO =======")
        print("1. Ingresar a su cuenta")
        print("2. Registrarse como nuevo usuario")
        print("3. Salir")

        opcion = int(input("Ingrese el número de opción que desee: "))

        if opcion == 1:
            cliente = Cliente("", "", "", "", "", "", "", "")
            if cliente.iniciar_sesion():
                print("Inicio de sesión exitoso.\n")
                return cliente  # Devuelve el cliente para usar en el menú principal
            else:
                print("Correo o contraseña incorrectos. Intente nuevamente.\n")
        elif opcion == 2:
            cliente = Cliente("", "", "", "", "", "", "", "")
            cliente.registrar_usuario()
        elif opcion == 3:
            print("Gracias por visitar nuestra tienda. ¡Hasta pronto!")
            exit()
        else:
            print("Opción inválida. Por favor, ingrese un número válido del menú.\n")


def menu_principal():
 while True:
    try:
        print("======= MENÚ DE COMPRA =======")
        print("1. Registrar Usuario")
        print("2. Ver carrito")
        print("3. Ver galería de productos")
        print("4. Agregar producto al carrito")
        print("5. Salir")

        opcion = int(input("Ingrese el número de opción que desee: "))
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_informacion_cliente(cliente1)
        elif opcion == "3":
            mostrar_carrito_cliente(cliente1)
        elif opcion == "4":
            mostrar_galeria_productos(productos)
        elif opcion == "5":
            
            print("Gracias por utilizar nuestro servicio de compra. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido del menú.\n")
    except ValueError:
        print("Error: Ingrese un número válido de opción.\n")
        
if __name__ == "__main__":
    # Cargar productos
    # Llamar al menú_inicio y pasar el cliente retornado al menú_principal
    cliente = menu_inicio()
    menu_principal(cliente)