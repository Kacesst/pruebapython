from cliente import Cliente
from carrito import Carrito
from producto import Producto

class Tienda:
    def __init__(self):
        self.clientes = {}  # Un diccionario para almacenar los clientes
        self.productos = []  # Una lista para almacenar los productos disponibles
        self.carritos = {}  # Un diccionario para almacenar los carritos de los clientes

    def agregar_cliente(self, nombre, apellido, correo, direccion, dni, telefono, tarjeta_credito, contrasena):
        cliente = Cliente(nombre, apellido, correo, direccion, dni, telefono, tarjeta_credito, contrasena)
        self.clientes[correo] = cliente

    def iniciar_sesion(self, correo, contrasena):
        if correo in self.clientes and self.clientes[correo].verificar_contrasena(contrasena):
            return self.clientes[correo]
        else:
            return None

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_galeria_productos(self):
        print("======= GALERÍA DE PRODUCTOS =======")
        for idx, producto in enumerate(self.productos, 1):
            print(f"{idx}. {producto.nombre} - ${producto.precio}")
        print()

    def obtener_producto_por_indice(self, indice):
        if 0 < indice <= len(self.productos):
            return self.productos[indice - 1]
        else:
            return None

    def mostrar_informacion_cliente(self, cliente):
        print("Información del cliente:")
        print(f"Nombre: {cliente.nombre} {cliente.apellido}")
        print(f"Correo: {cliente.correo}")
        print(f"Dirección: {cliente.direccion}")
        print(f"DNI: {cliente.dni}")
        print(f"Teléfono: {cliente.telefono}")
        print(f"Tarjeta de crédito: {cliente.tarjeta_credito}\n")

    def mostrar_carrito_cliente(self, cliente):
        if cliente.correo in self.carritos:
            carrito = self.carritos[cliente.correo]
            print("Carrito de", cliente.nombre, cliente.apellido + ":")
            for item in carrito.items:
                producto = item["producto"]
                cantidad = item["cantidad"]
                print(f"{producto.nombre} - Cantidad: {cantidad}")
            total_carrito = carrito.obtener_total_carrito()
            print(f"Total a pagar: ${total_carrito}\n")
        else:
            print("El carrito está vacío.\n")

    def agregar_producto_al_carrito(self, cliente, indice_producto, cantidad):
        producto = self.obtener_producto_por_indice(indice_producto)
        if producto:
            if cliente.correo not in self.carritos:
                self.carritos[cliente.correo] = carrito()
            carrito = self.carritos[cliente.correo]
            carrito.agregar_producto(producto, cantidad)
            print("Producto agregado al carrito.\n")
        else:
            print("El producto no existe o el índice es inválido.\n")

    def mostrar_menu_principal(self):
        while True:
            print("======= MENÚ DE COMPRA =======")
            print("1. Iniciar sesión")
            print("2. Registrarse")
            print("3. Ver galería de productos")
            print("4. Ver información del cliente")
            print("5. Ver carrito")
            print("6. Agregar producto al carrito")
            print("7. Salir")

            opcion = int(input("Ingrese el número de opción que desee: "))

            if opcion == 1:
                correo = input("Ingrese su correo electrónico: ")
                contrasena = input("Ingrese su contraseña: ")
                cliente = self.iniciar_sesion(correo, contrasena)
                if cliente:
                    print("Inicio de sesión exitoso.\n")
                else:
                    print("Correo o contraseña incorrectos. Intente nuevamente.\n")
            elif opcion == 2:
                # Solicitar datos para registrar nuevo cliente
                nombre = input("Ingrese su nombre: ")
                apellido = input("Ingrese su apellido: ")
                correo = input("Ingrese su correo electrónico: ")
                direccion = input("Ingrese su dirección: ")
                dni = input("Ingrese su DNI: ")
                telefono = input("Ingrese su teléfono: ")
                tarjeta_credito = input("Ingrese el número de su tarjeta de crédito: ")
                contrasena = input("Ingrese su contraseña: ")

                self.agregar_cliente(nombre, apellido, correo, direccion, dni, telefono, tarjeta_credito, contrasena)
                print("Registro exitoso. Ahora puede iniciar sesión.\n")
            elif opcion == 3:
                self.mostrar_galeria_productos()
            elif opcion == 4:
                correo = input("Ingrese su correo electrónico: ")
                if correo in self.clientes:
                    self.mostrar_informacion_cliente(self.clientes[correo])
                else:
                    print("El correo ingresado no está registrado.\n")
            elif opcion == 5:
                correo = input("Ingrese su correo electrónico: ")
                if correo in self.clientes:
                    self.mostrar_carrito_cliente(self.clientes[correo])
                else:
                    print("El correo ingresado no está registrado.\n")
            elif opcion == 6:
                correo = input("Ingrese su correo electrónico: ")
                if correo in self.clientes:
                    self.mostrar_galeria_productos()
                    indice_producto = int(input("Ingrese el número de producto que desea agregar al carrito: "))
                    cantidad = int(input("Ingrese la cantidad que desea agregar al carrito: "))
                    self.agregar_producto_al_carrito(self.clientes[correo], indice_producto, cantidad)
                else:
                    print("El correo ingresado no está registrado.\n")
            elif opcion == 7:
                print("Gracias por utilizar nuestro servicio de compra. ¡Hasta pronto!")
                break
            else:
                print("Opción inválida. Por favor, ingrese un número válido del menú.\n")
