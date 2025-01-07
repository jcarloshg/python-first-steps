def get_produc(**datos):
    print(datos)
    print(datos['id'], datos["name"])


get_produc(id=1, name="Laptop", desc=203.20)

# output:
# {'id': 1, 'name': 'Laptop', 'desc': 203.2}
# 1 Laptop
