for num in range(5):
    print(f"{num}: ", "*" * num)

# Output:
# 0:
# 1: *
# 2: **
# 3: ***
# 4: ****
# 5: *****


numToFind = 10
for num in range(5):
    print(f"current number: {num}")
    if num == numToFind:
        print(f"number found: {num}")
        # this will stop the loop
        break

# this will be executed if the loop ends without a break
else:
    print(f"number not found: {numToFind}")

# Output:
# current number: 0
# current number: 1
# current number: 2
# current number: 3
# current number: 4
# number not found: 10

for char in "Course Python":
    print(char)

# Output:
# C
# o
# u
# r
# s
# e
#
# P
# y
# t
# h
# o
# n
