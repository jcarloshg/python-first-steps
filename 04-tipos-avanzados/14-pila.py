# Last in, First in

pila = []
pila.append("user_01")
pila.append("user_02")
pila.append("user_03")

print(pila)  # ['user_01', 'user_02', 'user_03']


pila.pop()
pila.pop()
print(pila)  # ['user_01']

if not pila:
    print("pila empty")
