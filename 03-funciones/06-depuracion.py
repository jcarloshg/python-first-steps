def largo(text):
    resultado = 0
    for _ in text:
        resultado += 1
    return resultado


print("Debugging...")
length = largo("Python")
print(length)  # Output: 1
