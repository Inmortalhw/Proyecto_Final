class Bacteria:
    def __init__(self, id, raza, energia=50, resistente=False, estado="activa"):
        self.id = id
        self.raza = raza
        self.energia = energia
        self.resistente = resistente
        self.estado = estado

    def alimentar(self, nutrientes):
        pass

    def dividirse(self):
        pass

    def morir(self):
        pass

    def mutar(self):
        pass
