class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def description(self):
        return f"Marca: {self.marca} - Modelo {self.modelo}"


class Carro(Vehiculo):
    def description(self):
        return f"Carro - {super().description()}"


class Moto(Vehiculo):
    def description(self):
        return f"Moto - {super().description()}"


class Bicicleta(Vehiculo):
    def description(self):
        return f"Bicicleta - {super().description()}"


carro = Carro("Ford", "MXZ-45")
moto = Moto("Yamaha", "Meteor 350")
bici = Bicicleta("Meteoro", "mountain 205")
print(carro.description())
print(moto.description())
print(bici.description())
