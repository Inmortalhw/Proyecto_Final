import random

class Bacteria:
    def __init__(self, id, raza, energia=50, resistente=False, estado="activa", consumo_reducido=False):
        self.id = id
        self.raza = raza
        self.energia = energia
        self.resistente = resistente
        self.estado = estado
        self.consumo_reducido = consumo_reducido 

# Método para alimentar a la bacteria con nutrientes
    def alimentar(self, nutrientes_disponibles):   
        if nutrientes_disponibles <= 0:
            return 0
    
        # Bacterias normales consumen más que las mutadas
        if self.consumo_reducido:
            consumo = min(random.randint(3, 5), nutrientes_disponibles)
        else:
            consumo = min(random.randint(15, 25), nutrientes_disponibles)
    
        self.energia += consumo
        return consumo

    def consumir_energia(self, gasto=5):
        self.energia -= gasto
        if self.energia < 0:
            self.energia = 0
            print(f"{self.id} se ha quedado sin energía.")

# Método de reproducción de la bacteria
    def dividirse(self, probabilidad_mutacion=0.05 ): # Probabilidad de mutación del 5%
        if self.energia >= 60:
            energia_division = self.energia // 2 # Divide su energía a la mitad
            self.energia = energia_division

            hija = Bacteria(
                id=f"{self.id}-hija",
                raza=self.raza,
                energia=energia_division,
                resistente=self.resistente if random.random() < 0.95 else False, # La hija puede heredar la resistencia
                consumo_reducido=self.consumo_reducido if random.random() < 0.95 else False, # La hija puede heredar el consumo reducido
                estado="activa"
            )
            
            if random.random() < probabilidad_mutacion:
                hija.mutar() # Hija mutacion nueva

            return hija
        else:
            print(f"{self.id} no tiene suficiente energía para dividirse.")
            return None

    def morir(self, en_zona_antibiotica=False):
        if self.energia < 10: # Si la energía es menor a 10, la bacteria muere
            self.estado = "muerta"
            return True

        if en_zona_antibiotica and not self.resistente:
            probabilidad_supervivencia = 0.15
            if random.random() > probabilidad_supervivencia: 
                self.estado = "muerta"
                print(f"{self.id} ha muerto por el antibiótico.")
                return True
            else:
                print(f"{self.id} ha sobrevivido al antibiótico.")
        return False

    def mutar(self):
        tipo = random.choice(["resistencia", "consumo_reducido", "mutacion_neutra"])

        if tipo == "resistencia":
            self.resistente = True
            print(f"{self.id} ha mutado y ahora es resistente.")

        elif tipo == "consumo_reducido":
            self.consumo_reducido = True
            print(f"{self.id} ha mutado y ahora consume menos energía al alimentarse.")

        else:
            print(f"{self.id} ha mutado de forma neutral, sin cambios significativos.")