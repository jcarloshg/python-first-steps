
# classmethod -> makes one method be part from the class

class Perro:

    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("guau!")

    # create instances from Perro
    @classmethod
    def factory(cls):
        return cls("Firu", 5)


Perro.habla()  # guau!
perro_01 = Perro.factory()
# name: Firu, patas: 4
print(f"name: {perro_01.nombre}, patas: {perro_01.patas}")
