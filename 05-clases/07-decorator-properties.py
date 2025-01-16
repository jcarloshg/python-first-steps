
class Perro:

    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def name(self):
        print("in getter name")
        return self.__nombre

    @name.setter
    def name(self, new_name):
        print(f"in setter name: {new_name}")
        if new_name.strip():
            self.__nombre = new_name
        return

    def habla(self):
        print("guau!")


mi_perro_01 = Perro("Firu")
print(mi_perro_01.name)
mi_perro_01.name = "Nacho"
print(mi_perro_01.name)

# in getter name
# Firu
# in setter name: Nacho
# in getter name
# Nacho
