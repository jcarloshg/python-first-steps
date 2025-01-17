
class CajaRegistradora:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio):
        self.productos.append({"nombre": nombre, "price": precio})

    def obtener_total(self):
        return sum(producto['price'] for producto in self.productos)

    def dar_cambio(self, pago):
        total = self.obtener_total()
        if pago >= total:
            self.productos.clear()
            return pago - total
        return "Pago insuficiente"

    def listar_productos(self):
        return self.productos

    def __str__(self):
        return f"caja with {len(self.productos)} products and total: {self.obtener_total()}"


class Cuentas:
    def __init__(self):
        self.cuentas = []

    def agregar_cuenta(self, caja_registradora):
        self.cuentas.append(caja_registradora)

    def obtener_total_cuentas(self):
        return sum(cuenta.obtener_total() for cuenta in self.cuentas)

    def obtener_ticket_promedio(self):
        if not self.cuentas:
            return 0
        return self.obtener_total_cuentas() / len(self.cuentas)

    def listar_cuentas(self):
        return self.cuentas


caja_01 = CajaRegistradora()
caja_01.agregar_producto("Manzana", 0.5)
caja_01.agregar_producto("Pan", 1.0)


caja_02 = CajaRegistradora()
caja_02.agregar_producto("Banana", 0.5)
caja_02.agregar_producto("Bottle water", 3.0)

cuentas = Cuentas()
cuentas.agregar_cuenta(caja_01)
cuentas.agregar_cuenta(caja_02)
print(cuentas.obtener_total_cuentas())
print(cuentas.obtener_ticket_promedio())
for caja in cuentas.listar_cuentas():
    print(caja)
