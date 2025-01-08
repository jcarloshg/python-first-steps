
# .sort() -> Ordena la lista
# sorted() -> Devuelve una nueva lista ordenada

numbers_01 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

numbers_01.sort()
print(numbers_01)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
numbers_01.sort(reverse=True)
print(numbers_01)  # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]


numbers_02 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

sorted_numbers = sorted(numbers_02)
sorted_numbers_desc = sorted(numbers_02, reverse=True)
print(sorted_numbers)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
print(sorted_numbers_desc)  # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]


usuarios = [
    ["Ana", 20],
    ["Juan", 5],
    ["Pedro", 2],
    ["Maria", 16]
]


# def ordenar_por_edad(usuario):
#     return usuario[1]
# usuarios.sort(key=ordenar_por_edad, reverse=True)
# print(usuarios)  # [['Ana', 20], ['Maria', 16], ['Juan', 5], ['Pedro', 2]]

usuarios.sort(key=lambda usuario: usuario[1], reverse=True)
print(usuarios)  # [['Ana', 20], ['Maria', 16], ['Juan', 5], ['Pedro', 2]]
