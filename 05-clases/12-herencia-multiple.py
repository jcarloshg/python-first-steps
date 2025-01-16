
# The herency is giving from right to left
# the method eat from Perro is gonna
# overwrite over eat from Animal

#
# Bad practice
#

class Animal:
    def eat(self):
        print("some animal is eating")


class Perro():
    def eat(self):
        print("dog is eating")


class Cerdo(Perro, Animal):
    def sleep(self):
        print("is sleep")


pig = Cerdo()
pig.eat()


#
# Good practice
#   - each class must do one a unique task

class Walker:
    def walk(self):
        print("is walking")


class Flying:
    def fly(self):
        print("is flying")


class Swimmer:
    def swim(self):
        print("is swimming")


class Duck(Walker, Flying, Swimmer):
    def __init__(self):
        return


class Pig(Walker):
    def __init__(self):
        return


class Dog(Walker, Swimmer):
    def __init__(self):
        return


print("\n duck")
duck = Duck()
duck.fly()
duck.walk()
duck.swim()


print("\n pig")
pig = Pig()
pig.walk()

print("\n dog")
dog = Dog()
dog.swim()
dog.walk()


# OUTPUT:
#  duck
# is flying
# is walking
# is swimming

#  pig
# is walking

#  dog
# is swimming
# is walking
