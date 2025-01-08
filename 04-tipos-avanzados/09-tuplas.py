
# concat tuples
numbers = (1, 2, 3) + (6, 7, 8)
print(numbers)  # (1, 2, 3, 6, 7, 8)


# listo to tuples
numbers_01 = tuple(["hola", "mundo"])
print(numbers_01)  # ('hola', 'mundo')

# cut the tuple
short_tuple = numbers[:4]
print(short_tuple)  # (1, 2, 3, 6)

# desempaquetar tuple
first, second, *other = numbers
print(first, second, other)  # 1 2 [3, 6, 7, 8]

# iterar a tuple
for item in numbers:
    print(item)

# modify
listModified = list(numbers)
listModified[0] = 999
tupleModified = tuple(listModified)
print(tupleModified)  # (999, 2, 3, 6, 7, 8)
