mascotas = ["perro", "gato", "conejo", "tortuga", "hamster", "perro"]

print(mascotas.index("gato"))  # 1
# print(mascotas.index("Loro"))  # ValueError: 'Loro' is not in list

if "Loro" in mascotas:
    print(mascotas.index("Loro"))


print(mascotas.count("perro"))  # 2
