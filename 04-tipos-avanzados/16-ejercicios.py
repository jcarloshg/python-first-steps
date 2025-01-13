import random
import math

# Elobjetivodeesteejercicioescrearunprogramaquegenereeimprimaunticketdecompraapartirdeunalistadeproductos.Cadaproductoestárepresentadoporundiccionarioconunnombreyunprecio.Elprogramadebecalcularlacantidaddecadaproducto,elsubtotaldecadaunoyeltotaldelacompra.

productos = [
    {'nombre': 'Manzana', 'precio': 0.5},
    {'nombre': 'Manzana', 'precio': 0.5},
    {'nombre': 'Pan', 'precio': 1.0},
    {'nombre': 'Leche', 'precio': 1.5}
]


def generar_ticket(products: list) -> dict:

    ticket = {}

    for product in products:

        product_name = product["nombre"]
        product_cost = product["precio"]

        if product_name in ticket:
            ticket[product_name]['count'] += 1

        if product_name not in ticket:
            ticket[product_name] = {
                'count': 1,
                'cost': product_cost,
            }

    total = 0

    print("-----------------")
    print("Ticket de compra")
    print("-----------------")
    for product, product_data in ticket.items():
        product_name = product
        product_cost = product_data["cost"]
        product_units = product_data["count"]
        product_total = product_cost * product_units
        # Manzana x2 - $1.00
        print(f"{product_name} x{product_units} - ${product_total}")
        total += product_total

    print("-----------------")
    print(f"Total = {total}")
    print("-----------------")

    return {}


generar_ticket(productos)

# Esteejercicioseenfocaenidenti@icaralosclientesquecali@icanparaunapromoción.Losclientescali@icansielmontodesuscomprasesmayoroiguala150dólares.


def aplicar_promocion(buys):
    clients = []
    for client_id, buy_total in buys.items():
        if buy_total >= 150:
            clients.append(client_id)
    return clients


compras = {'Cliente1': 200, 'Cliente2': 100, 'Cliente3': 180}

clientes_promocion = aplicar_promocion(compras)
# ['Cliente1', 'Cliente3']
print(clientes_promocion)


# En este ejercicio, adems de identiicar a los clientes que caliican para la promocin, se les aplica un descuento del 10%. El programa retorna:

def aplicar_promocion_02(buyers: dict) -> list:

    discount = 0.10
    total_flag = 150

    clients = [
        monto
        for client_id, monto in buyers.items()
        if monto >= total_flag
    ]

    clients_with_discount = {
        client: monto
        for client, monto in buyers.items()
        if monto >= total_flag
    }

    for client, total in clients_with_discount.items():
        new_total = total - (total * discount)
        clients_with_discount[client] = new_total

    list_to_return = [
        clients,
        clients_with_discount
    ]

    return list_to_return


compras = {
    'Cliente1': 200,
    'Cliente2': 100,
    'Cliente3': 180
}

resultado = aplicar_promocion_02(compras)
# [['Cliente1', 'Cliente3'], {'Cliente1': 180.0, 'Cliente3': 162.0}]
print(resultado)

# Este ejercicio calcula el costo total de la promocin, es decir, la suma de los descuentos aplicados a los clientes elegibles.
compras = {
    'Cliente1': 200,
    'Cliente2': 100,
    'Cliente3': 180
}


def calcular_costo_promocion(compras: dict) -> float:

    total_flag = 150
    discount = 0.10
    promotion_total = 0

    for _, total in compras.items():
        if total >= total_flag:
            promotion_total += total * discount

    return promotion_total


costo_promocion = calcular_costo_promocion(compras)
print(costo_promocion)  # 38.0


# Vamos a mejorar un ejercicio de una seccin anterior, este ejercicio simula el lanzamiento de un dado una cantidad
# especica de veces. El programa debe calcular la frecuencia de cada cara en porcentaje.

def tirar_dados(times: int) -> dict:

    faces = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for _ in range(times):
        faces[random.randint(1, 6)] += 1

    for face, face_times in faces.items():

        percentage = 0
        if face_times != 0:
            percentage = (face_times / times)*100

        print(f"Cara: {face}, times: {face_times}, percentage: {percentage}%")

    return


tirar_dados(1000)

# Este ejercicio organiza una lista de cursos en tres grupos segn su estado:


def mostrar_cursos_por_estado(courses: list):

    in_progress = "en progreso"
    completed = "completado"
    not_started = "no iniciado"

    state_name = "estado"

    in_progress_list = list(
        filter(
            lambda course: course[state_name] == in_progress,
            courses
        )
    )
    in_progress_name_list = list(
        map(
            lambda course: course["nombre"],
            in_progress_list
        )
    )

    completed_list = list(
        filter(
            lambda course: course[state_name] == completed,
            courses
        )
    )
    completed_name_list = list(
        map(
            lambda course: course["nombre"],
            completed_list
        )
    )

    not_started_list = list(
        filter(
            lambda course: course[state_name] == not_started,
            courses
        )
    )
    not_started_name_list = list(
        map(
            lambda course: course["nombre"],
            not_started_list
        )
    )

    en_progreso = filter(
        lambda curso: curso['estado'] == 'en progreso', cursos)
    # Usando listas de comprensión.
    completados = [
        curso for curso in cursos if curso['estado'] == 'completado']
    no_iniciados = [
        curso for curso in cursos if curso['estado'] == 'no iniciado']

    print("In progress:")
    for name in in_progress_name_list:
        print(f"    - {name}")

    print("Completed:")
    for name in completed_name_list:
        print(f"    - {name}")

    print("In progress:")
    for name in not_started_name_list:
        print(f"    - {name}")


cursos = [
    {"nombre": "HTML: Sin Fronteras", "estado": "en progreso"},
    {"nombre": "CSS3: Sin Fronteras", "estado": "completado"},
    {"nombre": "SQL: Sin Fronteras", "estado": "no iniciado"},
    {"nombre": "Python: HTML, CSS, Flask, MySQL", "estado": "en progreso"},
    {"nombre": "Aprende Javascript, HTML5, CSS3 y NodeJS desde cero",
        "estado": "completado"},
    {"nombre": "React - Guía definitiva: hooks, router, redux, next + Proyectos",
     "estado": "no iniciado"},
    {"nombre": "TypeScript: sin fronteras", "estado": "completado"},
    {"nombre": "Ultimate Python", "estado": "en progreso"},
    {"nombre": "Ultimate Linux", "estado": "completado"},
    {"nombre": "Ultimate Docker", "estado": "no iniciado"},
    {"nombre": "Ultimate GIT + GITHUB", "estado": "en progreso"},
    {"nombre": "Ultimate JavaScript", "estado": "completado"},
    {"nombre": "Ultimate React", "estado": "no iniciado"},
    {"nombre": "Ultimate Java", "estado": "en progreso"}
]
mostrar_cursos_por_estado(cursos)


# Este ejercicio calcula dos estadsticas importantes de una lista de nmeros:
#   1. La mediana: Es el valor que separa la mitad superior de la mitad inferior de una lista ordenada de nmeros.
#       Si la lista tiene un nmero par de elementos, la mediana es el promedio de los dos valores centrales.
#   2. La moda: El valor que aparece con mayor frecuencia.

def calcular_mediana(numbers: list) -> int:

    list_length = len(numbers)
    list_middle_module = list_length % 2
    list_middle = math.ceil(list_length/2) - 1

    if list_length % 2 is 0:
        first_number = numbers[list_middle_module]
        second_number = numbers[list_middle_module + 1]
        promedio = (first_number + second_number) / 2
        return promedio

    if list_length % 2 is not 0:
        return numbers[list_middle]


def calcular_moda(numbers: list) -> int:

    aux_dict = {}
    for number in numbers:

        if number in aux_dict:
            aux_dict[number] += 1

        if number not in aux_dict:
            aux_dict[number] = 0

    moda = {"number": 0, "times": 0}
    for number, times in aux_dict.items():

        if times > moda["times"]:
            moda = {"number": number, "times": times}

    return moda["number"]
    # return max(frecuencia, key=frecuencia.get)


def calcular_mediana_y_moda(numbers: list):
    mediana = calcular_mediana(numbers)
    moda = calcular_moda(numbers)
    return mediana, moda


datos = [1, 2, 2, 3, 4]
mediana, moda = calcular_mediana_y_moda(datos)
print(mediana, moda)  # 2, 2
datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
mediana, moda = calcular_mediana_y_moda(datos)
print(mediana, moda)  # 7, 10


# Busca tareas especicas en una lista utilizando dos mtodos:
#       1. Por ID
#       2. Por texto contenido en la descripcin.

def buscar_tarea_por_id(tasks: list, id: int):
    for task in tasks:
        if task["id"] == id:
            return task


def buscar_tareas_por_texto(tasks: list, string: str) -> list:
    task_filtered = []

    for task in tasks:
        is_the_string = task["descripcion"].lower().find(string.lower())
        if is_the_string > 0:
            task_filtered.append(task)

    return task_filtered


tareas = [
    {"id": 1, "descripcion": "Lavar los platos"},
    {"id": 2, "descripcion": "Sacar la basura"},
    {"id": 3, "descripcion": "Limpiar el baño"},
    {"id": 4, "descripcion": "Hacer la cama"},
    {"id": 5, "descripcion": "Cocinar la cena"},
    {"id": 6, "descripcion": "Pasear al perro"},
    {"id": 7, "descripcion": "Hacer la compra"},
    {"id": 8, "descripcion": "Planchar la ropa"},
    {"id": 9, "descripcion": "Regar las plantas"},
    {"id": 10, "descripcion": "Lavar el coche"}
]


print("buscar_tarea_por_id", buscar_tarea_por_id(tareas, 1))
print("buscar_tareas_por_texto", buscar_tareas_por_texto(tareas, "Co"))
