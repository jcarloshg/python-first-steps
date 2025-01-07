saludo = "Hola mundo"


def saludar():
    global saludo
    saludo = "Hola desde la función"
    print(saludo)


def otroSaludo():
    saludo = "Hola desde otra función"
    print(saludo)


print(saludo)  # Output: Hola mundo
saludar()  # Output: Hola desde la función
print(saludo)  # Output: Hola desde la función
