

# Descripción
# Aquse implementa una clase CuentaBancaria que maneja depsitos, retiros y saldos, con excepciones
# personalizadas para manejar errores como retiros de cantidades negativas o superiores al saldo disponible.

class ErrorRetiro(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class CuentaBancaria:
    def __init__(self, identifier, name, balance):
        self.__identifier = identifier
        self.__name = name
        self.__balance = balance

    def mostrar_saldo(self):
        print(f"The balance from {self.__name} is: ${self.__balance}")

    def depositar(self, money):
        self.__balance += money

    def retirar(self, money):

        if money < 0:
            raise ErrorRetiro(
                "La cantidad a retirar debe ser positiva.",
                400
            )

        if money > self.__balance:
            raise ErrorRetiro(
                "Fondos insuficientes para realizar el retiro.",
                401
            )


try:
    cuenta = CuentaBancaria("123456789", "Juan Perez", 1000)
    cuenta.mostrar_saldo()
    cuenta.depositar(500)
    cuenta.retirar(2000)
except ErrorRetiro as e:
    print(e)
try:
    cuenta.retirar(-100)
except ErrorRetiro as e:
    print(e)


# OUTPUT
# The balance from Juan Perez is: $1000
# ('Fondos insuficientes para realizar el retiro.', 401)
# ('La cantidad a retirar debe ser positiva.', 400)
