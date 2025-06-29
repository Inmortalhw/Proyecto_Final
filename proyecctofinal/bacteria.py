import random

class Bacteria:
    def __init__(self, id, raza, energia=50, resistente=False, estado="activa"):
        self.id = id
        self.raza = raza
        self.energia = energia
        self.resistente = resistente
        self.estado = estado

# Método para alimentar a la bacteria con nutrientes
    def alimentar(self, nutrientes):
        consumo = random.randint(15, 25) # Consumo aleatorio de nutrientes entre 15 y 25
        self.energia += consumo
        return consumo

    def dividirse(self):
        pass

    def morir(self):
        if self.energia < 10: # Si la energía es menor a 10, la bacteria muere
            self.estado = "muerta"
            return True
        return False


    def mutar(self):
        pass
