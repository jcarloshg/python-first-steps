
# Propiedades

class Perro:

    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f'{self.nombre} dice : guaf!')


Perro.patas = 5
mi_perro = Perro("Roberto", 5)
print(f"{mi_perro.nombre} tiene num patas: {mi_perro.patas}")

mi_perro_2 = Perro("Filo", 5)
mi_perro_2.patas = 3
print(f"{mi_perro_2.nombre} tiene num patas: {mi_perro_2.patas}")
