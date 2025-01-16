class Perro:            # convention of pascal case
    def habla(self):    # all methods must have the argument self
        print('guaf!')


mi_perro = Perro()
mi_perro.habla()

print(isinstance(mi_perro,  Perro))  # True
