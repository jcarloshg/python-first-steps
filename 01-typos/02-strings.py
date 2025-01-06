nombre_curso = 'Ultimate python'
description = """
    Este curso es el mejor curso de python en español.
    Este es un nuevo y excelente curso de python.
"""

print(nombre_curso, description)

log = len(nombre_curso)
print(log)


# HERE
# Print the first character of the course name
print(nombre_curso[0])

# cut the words "Ultimate python" and print them
print(nombre_curso[0:4])  # position 0 to 4
print(nombre_curso[4:])  # position 4 to the end
print(nombre_curso[:8])  # position 0 to 8
print(nombre_curso[:])  # position 0 to the end
