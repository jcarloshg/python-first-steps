n1 = input("Ingrese el primer número: ")
n2 = input("Ingrese el segundo número: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
division = n1 / n2

respuesta = f"""
Para los números {n1} y {n2}:
    La suma de los números es: {suma}
    La resta de los números es: {resta}
    La multiplicación de los números es: {multi}
    La división de los números es: {division}
"""

print(respuesta)
