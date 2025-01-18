class Error404(Exception):
    "Not found the resourse"

    __type = "ERROR_404"

    def __init__(self, _identifier):
        self._identifier = _identifier

    @property
    def type(self):
        return self.__type

    def __str__(self):
        return f"Not found item with id: {self._identifier}. 😞"

    @classmethod
    def is_instance_from(self, instance):
        try:
            return True if self.__type == instance.type else False
        except Exception as e:
            return False


def get_item_by_id(_id):
    if _id <= 0:
        raise Error404(_id)

    return {"_id": _id, "name": "Super Meteor 350"}


try:
    get_item_by_id(-10)
except Exception as e:
    if Error404.is_instance_from(e):
        print(e)
    else:
        print("Something was wrong, please try later.")
