animal = "   cerDITO contento  "
print(animal.upper())  # resultado:    CERDITO CONTENTO
print(animal.lower())  # resultado:    cerdito contento
print(animal.title())  # resultado:    Cerdito Contento
print(animal.capitalize())  # resultado:    Cerdito contento
print(animal.strip())  # resultado: cerDITO contento
print(animal.strip().capitalize())  # resultado: Cerdito contento
print(animal.rstrip())  # resultado:    cerDITO contento
print(animal.lstrip())  # resultado: cerDITO contento
print(animal.find("cer"))  # resultado: 3, retorna indice
print(animal.find("pe"))  # resultado: -1, No existe, retorna indice -1
print(animal.replace("cerDITO", "gato"))  # resultado:    gato contento
print("cer" in animal)  # resultado: True, retorna True si existe
print("años" not in animal)  # resultado: False, retorna True si no existe
