# Descripción
# En este ejercicio, se implementa una clase CajaRegistradora que permite gestionar productos y pagos. La clase
# incluye mtodos para agregar productos, calcular el total y dar cambio. Si el cliente no proporciona suiciente dinero,
# se lanza una excepcin

class CajaRegistradora:
    __products = []

    def __init__(self):
        self.__products = []

    def agregar_producto(self, name, price):
        self.__products.append({"name": name, "price": price})

    def obtener_total(self):
        total = sum(product["price"] for product in self.__products)
        return total

    def dar_cambio(self, money):
        total = self.obtener_total()
        remaining_money = money - total
        if remaining_money < 0:
            raise Exception("there is not enough money")
        else:
            return remaining_money


caja = CajaRegistradora()
caja.agregar_producto('Manzana', 0.5)
caja.agregar_producto('Pan', 1)
print("Total:", caja.obtener_total())
try:
    print("Cambio:", caja.dar_cambio(2))
    print("Cambio:", caja.dar_cambio(1))
except Exception as e:
    print(e)

# OUTPUT
# Total: 1.5
# Cambio: 0.5
# there is not enough money
