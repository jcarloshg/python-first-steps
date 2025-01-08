
usuarios = [
    ["Ana", 20],
    ["Juan", 5],
    ["Pedro", 2],
    ["Maria", 16]
]


# obtener unicamente edad
usuarios_01 = []
for usuario in usuarios:
    usuarios_01.append(usuario[0])

print(usuarios_01)  # ['Ana', 'Juan', 'Pedro', 'Maria']

# obtener unicamente edad
usuarios_02 = [usuario[0] for usuario in usuarios]
print(usuarios_02)  # ['Ana', 'Juan', 'Pedro', 'Maria']


# filtrar mayores de 15 anios
usuarios_03 = [usuario[0] for usuario in usuarios if usuario[1] > 15]
print(usuarios_03)  # ['Ana', 'Maria']


usuarios_01 = [
    ["Ana", 20],
    ["Juan", 5],
    ["Pedro", 2],
    ["Maria", 16]
]

# map
users_mapped = list(map(lambda user: user[0], usuarios_01))
print(users_mapped)  # ['Ana', 'Juan', 'Pedro', 'Maria']

# filter
users_filtered = list(filter(lambda user: user[1] > 15, usuarios_01))
print(users_filtered)  # [['Ana', 20], ['Maria', 16]]
