
def mostrar_menu_carrito(cliente):
    while True:
        print("\n======= MENÚ DEL CARRITO =======")
        print("1. Mostrar carrito")
        print("2. Agregar producto al carrito")
        print("3. Eliminar producto del carrito")
        print("4. Finalizar compra")
        print("5. Volver al menú principal")

        opcion = int(input("Ingrese el número de opción que desee: "))

        if opcion == 1:
            mostrar_carrito_cliente(cliente)
        elif opcion == 2:
            agregar_producto_al_carrito(cliente, productos)
        elif opcion == 3:
            eliminar_producto_del_carrito(cliente)
        elif opcion == 4:
            finalizar_compra(cliente)
        elif opcion == 5:
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido del menú.\n")

def mostrar_carrito_cliente(cliente):
    print("\nCarrito de", cliente.nombre, cliente.apellido + ":")
    for item in cliente.carrito.productos:
        producto = item["producto"]
        cantidad = item["cantidad"]
        print(f"{producto.nombre} - Cantidad: {cantidad}")
    total_carrito = cliente.carrito.obtener_total_carrito()
    print(f"Total a pagar: ${total_carrito}\n")

def agregar_producto_al_carrito(cliente, productos):
    mostrar_galeria_productos(productos)
    numero_producto = int(input("Ingrese el número de producto que desea agregar al carrito: "))
    producto_seleccionado = productos[numero_producto - 1]
    cantidad = int(input("Ingrese la cantidad que desea agregar al carrito: "))
    cliente.carrito.agregar_producto(producto_seleccionado, cantidad)
    print("Producto agregado al carrito.\n")

def eliminar_producto_del_carrito(cliente):
    mostrar_carrito_cliente(cliente)
    numero_producto = int(input("Ingrese el número de producto que desea eliminar del carrito: "))
    cliente.carrito.eliminar_producto(numero_producto)
    print("Producto eliminado del carrito.\n")

def finalizar_compra(cliente):
    mostrar_carrito_cliente(cliente)
    confirmacion = input("¿Está seguro que desea finalizar la compra? (s/n): ")
    if confirmacion.lower() == "s":
        cliente.finalizar_compra()
        print("Compra realizada con éxito.\n")
    else:
        print("Compra cancelada.\n")

# Código para cargar la lista de productos y clientes

while True:
    print("======= MENÚ PRINCIPAL =======")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")

    opcion = int(input("Ingrese el número de opción que desee: "))

    if opcion == 1:
        # Código para iniciar sesión
        cliente = None  # Reemplazar esto con el cliente que ha iniciado sesión
        if cliente is not None:
            print(f"Bienvenido, {cliente.nombre} {cliente.apellido}!\n")
            mostrar_menu_carrito(cliente)
        else:
            print("Inicio de sesión fallido. Por favor, verifique sus credenciales.\n")
    elif opcion == 2:
        # Código para registrarse
        # (Agrega un nuevo cliente a la lista de clientes)
        print("Registro de nuevo cliente.")
    elif opcion == 3:
        print("Gracias por utilizar nuestro servicio de compra. ¡Hasta pronto!")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número válido del menú.\n")
