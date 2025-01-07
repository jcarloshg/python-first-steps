def hola(name, lastName):
    print("Hola Mundo")
    print(f"Ejemplo de funciones {name} {lastName}")


hola("Jose", "Huerta")
hola("Fernanda", "Reyes")

# output:
# Hola Mundo
# Ejemplo de funciones Jose Huerta
# Hola Mundo
# Ejemplo de funciones Fernanda Reyes


def holaOptional(name, lastName="Feliz"):
    print("Hola Mundo")
    print(f"Ejemplo de funciones {name} {lastName}")


holaOptional("Jose")
holaOptional("Fernanda", "Reyes")

# output:
# Hola Mundo
# Ejemplo de funciones Jose Feliz
# Hola Mundo
# Ejemplo de funciones Fernanda Reyes


holaOptional(lastName="Huerta", name="Jose")
# output:
# Hola Mundo
# Ejemplo de funciones Jose Huerta
