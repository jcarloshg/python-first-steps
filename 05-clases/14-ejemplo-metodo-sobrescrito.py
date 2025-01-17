class Model:
    table = False

    def __init__(self):
        if not self.table:
            print("error: Set up the table name")

    def save(self):
        print(f"saving the table {self.table} in DB")

    @classmethod
    def get_by_id(self, _id):
        print(f"Searching by the id: {_id} in table: {self.table}")


class Usuario(Model):
    table = "Users"


usuario_01 = Usuario()
usuario_01.save()
usuario_01.get_by_id(123)
Usuario.get_by_id(456)

# OUTPUT
# saving the table Users in DB
# Searching by the id: 123 in table: Users
# Searching by the id: 456 in table: Users
