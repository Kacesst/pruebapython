import json
class Producto:
    def __init__(self, nombre, precio, descripcion, categoria, color, talle, stock, foto, materiales, diseño, colaboracion_con=None):
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
        self.colaboracion_con = colaboracion_con

    def agregar_stock(self, cantidad):
        self.stock += cantidad
        
    def mostrar_informacion(self):
        print(f"{self.nombre} - Categoría: {self.categoria} - Talle: {self.talle} - Color: {self.color}")
        print(f"Precio: ${self.precio} - Stock disponible: {self.stock}")
        print(f"Descripción: {self.descripcion}")
        print(f"Foto: {self.foto}")
        print(f"Materiales: {self.materiales}")
        print(f"Diseño: {self.diseño}")
    def to_json(self):
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "descripcion": self.descripcion,
            "categoria": self.categoria,
            "color": self.color,
            "talle": self.talle,
            "stock": self.stock,
            "foto": self.foto,
            "materiales": self.materiales,
            "diseño": self.diseño
        }

class Zapatilla(Producto):
    def __init__(self, nombre, precio, descripcion, categoria, color, talle, stock, foto, marca, modelo, colaboracion_con=None):
        super().__init__(nombre, precio, descripcion, categoria, color, talle, stock, foto, marca, modelo, colaboracion_con)
        self.marca = marca
        self.modelo = modelo
        
# Clase Gorra, derivada de Producto
class Gorra(Producto):
    def __init__(self, nombre, precio, descripcion, categoria, color, talle, stock, foto, colaboracion_con=None):
        super().__init__(nombre, precio, descripcion, categoria, color, talle, stock, foto, colaboracion_con)

# Clase Abrigo, derivada de Producto
class Abrigo(Producto):
    def __init__(self, nombre, precio, descripcion, categoria, color, talle, stock, material, foto, marca, colaboracion_con=None):
        super().__init__(nombre, precio, descripcion, categoria, color, talle, stock, foto, colaboracion_con)
        self.material = material
        self.marca = marca

# Clase Pantalón, derivada de Producto
class Pantalon(Producto):
    def __init__(self, nombre, precio, descripcion, categoria, color, talle, stock, estilo, foto, marca, colaboracion_con=None):
        super().__init__(nombre, precio, descripcion, categoria, color, talle, stock, foto, colaboracion_con)
        self.estilo = estilo
        self.marca = marca



