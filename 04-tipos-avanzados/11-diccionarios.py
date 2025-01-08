point = {"x": 10, "y": 5}
print(point)  # {'x': 10, 'y': 5}
print(point["x"])  # 10
print(point["y"])  # 5

if "lala" in point:
    print(f"it exists: ${point["lala"]}")

print(point.get("y"))
print(point.get("h", 1000))

# add elements
point["z"] = 2
print(point)  # {'x': 10, 'y': 5, 'z': 2}

# delete
del point["x"]
print(point)  # {'y': 5, 'z': 2}


point_01 = {"x": 10, "y": 5, "z": -2}

for item in point_01:
    print(f"item {item}, value: {point_01[item]}")

# output
# item x, value: 10
# item y, value: 5
# item z, value: -2

for item in point_01.items():
    print(item)

# output
# ('x', 10)
# ('y', 5)
# ('z', -2)


for key, value in point_01.items():
    print(f"{key} {value}")

# output
# x 10
# y 5
# z -2
