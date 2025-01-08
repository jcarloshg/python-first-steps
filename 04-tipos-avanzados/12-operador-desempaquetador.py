
list_01 = [1, 2, 3, 4, 5]

# both print the same thing
print(list_01[0], list_01[1], list_01[2], list_01[3], list_01[4])  # 1 2 3 4 5
print(*list_01)  # 1 2 3 4 5


# create new lists
list_02 = [6, 7, 8, 9, 10]
list_03 = [*list_01, 645, *list_02, 98]
print(list_03)  # [1, 2, 3, 4, 5, 645, 6, 7, 8, 9, 10, 98]


dictionary_01 = {"x": 4, "y": 6}
dictionary_02 = {"y": -4}

point = {**dictionary_01, **dictionary_02, "z": 12}
print(point)  # {'x': 4, 'y': -4, 'z': 12}
