# manage a set
first_set = {1, 1, 2, 2, 3, 4, 5}
print(first_set)  # {1, 2, 3, 4, 5}
first_set.add(5)
first_set.add(10)
print(first_set)  # {1, 2, 3, 4, 5, 10}
first_set.remove(2)
print(first_set)  # {1, 3, 4, 5, 10}

# create a set
numbers_02 = [1, 2, 3, 4, 678, 890, 234]
second_set = set(numbers_02)
print(second_set)  # {1, 2, 3, 4, 678, 234, 890}

# operations

# union
print(first_set | second_set)  # {1, 2, 3, 4, 5, 678, 10, 234, 890}

# intersection
print(first_set & second_set)  # {1, 3, 4}

# deference
#   remove the item from the first set comparing the second set
print(first_set - second_set)  # {10, 5}

# symmetric
#   drop the items repeated between the first set and second set
print(first_set ^ second_set)  # {2, 10, 5, 678, 234, 890}
