mascotas = ["perro", "gato", "conejo", "tortuga", "hamster", "perro"]

mascotas.insert(2, "loro")  # Inserta "loro" en el índice 2
# ['perro', 'gato', 'loro', 'conejo', 'tortuga', 'hamster', 'perro']
print(mascotas)

mascotas.append("pez")  # Añade "pez" al final de la lista
# ['perro', 'gato', 'loro', 'conejo', 'tortuga', 'hamster', 'perro', 'pez']

mascotas.remove("gato")  # Elimina la primera ocurrencia de "gato"
# ['perro', 'loro', 'conejo', 'tortuga', 'hamster', 'perro', 'pez']
mascotas.pop(3)  # Elimina y devuelve el elemento en el índice 3
# ['perro', 'loro', 'conejo', 'hamster', 'perro', 'pez']
mascotas.pop()  # Elimina y devuelve el último elemento
# ['perro', 'loro', 'conejo', 'hamster', 'perro']

del mascotas[1]  # Elimina el elemento en el índice 1
# ['perro', 'conejo', 'hamster', 'perro']

mascotas.clear()  # Elimina todos los elementos de la lista
# []

print(mascotas)
