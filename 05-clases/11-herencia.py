class Animal:
    def eat(self):
        print("is eating")


class Perro(Animal):
    def run(self):
        print("is running")


class Cerdo(Perro):
    def sleep(self):
        print("is sleep")


print("perro")
perro = Perro()
perro.run()
perro.eat()

# OUTPUT
# is running
# is eating

print("\npig")
pig = Cerdo()
pig.eat()
pig.run()
pig.sleep()

# OUTPUT
# is eating
# is running
# is sleep
