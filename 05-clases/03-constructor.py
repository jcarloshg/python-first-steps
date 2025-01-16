
# self have referencia a la instancia misma

class Perro:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f'{self.nombre} dice : guaf!')


mi_perro = Perro("Roberto", 5)  # Roberto dice : guaf!
mi_perro.habla()

mi_perro_2 = Perro("Firu", 5)  # Firu dice : guaf!
mi_perro_2.habla()
