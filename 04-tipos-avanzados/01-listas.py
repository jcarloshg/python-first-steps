numeros = [0, 1, 2, 3, 4, 5]
print(numeros)  # [0, 1, 2, 3, 4, 5]

letras = ['a', 'b', 'c', 'd', 'e']
print(letras)  # ['a', 'b', 'c', 'd', 'e']

palabras = ['hola', 'adios', 'gracias']
print(palabras)  # ['hola', 'adios', 'gracias']

booleanos = [True, False, True]
print(booleanos)  # [True, False, True]

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

ceros = [0] * 5
print(ceros)  # [0, 0, 0, 0, 0]
ceros_con_1 = [0] * 5 + [1]
print(ceros_con_1)  # [0, 0, 0, 0, 0, 1]
ceros_con_1_y_2 = [0, 1, 2] * 2
print(ceros_con_1_y_2)  # [0, 1, 2, 0, 1, 2]

alfanumerico = numeros + letras
print(alfanumerico)  # [0, 1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']

rango = list(range(1, 11))
print(rango)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chars = list('Taza de cafe')
print(chars)  # ['T', 'a', 'z', 'a', ' ', 'd', 'e', ' ', 'c', 'a', 'f', 'e']
