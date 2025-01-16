
# 1. add double __ to convert a property to private

class Perro:

    patas = 4

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def get_name(self):
        return self.__nombre

    def set_name(self, new_name):
        self.__nombre = new_name

    def habla(self):
        print("guau!")

    # create instances from Perro
    @classmethod
    def factory(cls):
        return cls("Firu", 5)


perro_01 = Perro.factory()
# print(perro_01.__nombre)  # this get us an error

print(f"name: {perro_01.get_name()}")  # name Firu
perro_01.set_name("Rodo")
print(f"new name: {perro_01.get_name()}")  # new name Rodo

# {'_Perro__nombre': 'Rodo', 'edad': 5}
# the private properties are going to be with the next structure
#   _{CLASS_NAME}__{PROPERTY_NAME}
print(perro_01.__dict__)
