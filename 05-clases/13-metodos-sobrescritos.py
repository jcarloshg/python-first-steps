class Ave:
    def __init__(self):
        print("in constructor Ave")
        self.volador = "is volador"

    def vuela(self):
        print("ave is flaying")


class Pato(Ave):

    def __init__(self):
        print("in constructor pato")
        super().__init__()
        self.nadador = "nadador"

    def vuela(self):
        super().vuela()
        print("pato is flying")


pato_01 = Pato()
pato_01.vuela()


# OUTPUT
# in constructor pato
# in constructor Ave
# ave is flaying
# pato is flying
