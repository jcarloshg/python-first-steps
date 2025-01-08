mascotas = ["perro", "gato", "conejo", "tortuga"]
print(mascotas)  # ['perro', 'gato', 'conejo']
print(mascotas[1])  # gato

mascotas[1] = "hamster"
print(mascotas)  # ['perro', 'hamster', 'conejo']

print(mascotas[:3])  # ['perro', 'hamster', 'conejo']
print(mascotas[1:])  # ['hamster', 'conejo']
print(mascotas[-1])  # tortuga

print(mascotas[::2])  # ['perro', 'conejo']
print(mascotas[1::2])  # ['hamster', 'tortuga']


numeros = range(21)
print(numeros[::2])  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(numeros[1::2])  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
