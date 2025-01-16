
# start and end with __
# are call without the user necessarily calling them
# more information
#   - https://rszalski.github.io/magicmethods/#representations

class Perro:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"This is a Perro. Name: {self.name}, age: {self.age}"

    def hablar(self):
        print(f"{self.name} say: guau!")


perro_01 = Perro("Chancho", 2)
print(perro_01)  # This is a Perro. Name: Chancho, age: 2

text = str(perro_01.__str__())
print(text)  # This is a Perro. Name: Chancho, age: 2
