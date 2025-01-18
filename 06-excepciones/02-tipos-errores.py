try:
    print('\n')
    int(input("Ingresa un número: "))
except ValueError as e:
    print('\n')
    print(e)
    print(f"type {type(e)}")

# OUTPUT
# Ingresa un número: asd
# invalid literal for int() with base 10: 'asd'
# type <class 'ValueError'>

try:
    print('\n')
    int(input("Ingresa un otro número: "))
except Exception as e:
    print('\n')
    print(e)
    print(f"type {type(e)}")

# OUTPUT
# Ingresa un otro número: qwe
# invalid literal for int() with base 10: 'qwe'
# type <class 'ValueError'>
