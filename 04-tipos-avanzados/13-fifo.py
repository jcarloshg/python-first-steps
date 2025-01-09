from collections import deque

fila = deque([1, 2, 3, 4])
fila.append(5)
fila.append(6)
fila.append(7)
print(fila)  # deque([1, 2, 3, 4, 5, 6, 7])

fila.popleft()
fila.popleft()
print(fila)  # deque([3, 4, 5, 6, 7])


fila_01 = deque([])
if not fila_01:
    print("empty fila")  # empty fila
