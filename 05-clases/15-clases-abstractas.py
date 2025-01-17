from abc import ABC, abstractmethod


class Model(ABC):

    @property
    @abstractmethod
    def table(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @classmethod
    def get_by_id(self, _id):
        print(f"Searching by the id: {_id} in table: {self.table}")


class Usuario(Model):
    table = "Users"

    def save(self):
        print(f"saving the table {self.table} in DB")


# model = Model()
# TypeError: Can't instantiate abstract class Model without an implementation for abstract methods 'save', 'table'

usuario_01 = Usuario()
usuario_01.save()
Usuario.get_by_id(987)
# OUTPUT
# saving the table Users in DB
# Searching by the id: 987 in table: Users
