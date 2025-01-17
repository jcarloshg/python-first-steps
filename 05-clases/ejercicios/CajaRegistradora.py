class CajaRegistradora:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio):
        self.productos.append({"nombre": nombre, "price": precio})

    def obtener_total(self):
        return sum(producto['price'] for producto in self.productos)
        # total = 0
        # for item in self.productos:
        #     total += item["price"]
        # return total

    def dar_cambio(self, pago):
        total = self.obtener_total()
        if pago >= total:
            self.productos.clear()
            return pago - total
        return "Pago insuficiente"

    def listar_productos(self):
        return self.productos


caja = CajaRegistradora()
caja.agregar_producto("Manzana", 0.5)
caja.agregar_producto("Pan", 1.0)
print(caja.listar_productos())
print(caja.obtener_total())
print(caja.dar_cambio(2.0))
print(caja.dar_cambio(1.0))
print(caja.listar_productos())
