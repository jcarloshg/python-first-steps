def suma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    print(resultado)


suma(1, 2, 3, 4, 5)  # 15
suma(1, 2, 3)  # 6
suma(1, 2)  # 3
suma(1)  # 1
