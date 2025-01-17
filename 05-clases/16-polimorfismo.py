from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def save(self):
        pass


class Client(Model):
    def save(self):
        print("saving Client")


class Secretary(Model):
    def save(self):
        print("saving Secretary")


def run_save_method(entities):
    for entity in entities:
        entity.save()


client = Client()
secretary = Secretary()

run_save_method([client, secretary])

# OUTPUT:
# saving Client
# saving Secretary

#
# Duck Typing
# Python doesn't verify the type of parameters.
# So, Python, at method run_save_item, knows that
# the argument entities is a list and each item from that list
# has the method save; and this method expects to get a property


class CartonBox:
    def save(self, thing):
        print(f"saving {thing} in CartonBox")


class WardrobeDrawer:
    def save(self, item):
        print(f"saving {item} in WardrobeDrawer")


def run_save_item(entities, item):
    for entity in entities:
        entity.save(item)


cartonBox = CartonBox()
wardrobeDrawer = WardrobeDrawer()

run_save_item([cartonBox, wardrobeDrawer], "cup")

# OUTPUT
# saving cup in CartonBox
# saving cup in WardrobeDrawer
