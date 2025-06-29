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

# Método de reproducción de la bacteria
    def dividirse(self):
        if self.energia >= 70:
            energia_division = self.energia // 2 # Divide su energía a la mitad
            self.energia = energia_division

            nueva_bacteria = Bacteria(
                id=f"{self.id}-hija",
                raza=self.raza,
                energia=energia_division,
                resistente=self.resistente,
                estado="activa"
            )
            return nueva_bacteria
        else:
            print(f"{self.id} no tiene suficiente energía para dividirse.")
            return None

    def morir(self):
        if self.energia < 10: # Si la energía es menor a 10, la bacteria muere
            self.estado = "muerta"
            return True
        return False

    def mutar(self):
        pass
