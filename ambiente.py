import numpy as np #importación de numpy para comenzar grilla
from bacteria import Bacteria #importación de la clase Bacteria
import random #importación de random para aleatorizar direcciones

class Ambiente:
    def __init__(self, filas, columnas):
        self.grilla = np.full((filas, columnas), None, dtype=object) #Grilla de tipo objetos sin nada
        self.nutrientes = np.full((filas, columnas), 40) #Grilla de nutrientes con valor 40
        self.factores = {
            "antibióticos": None
        }

    def actualizar_nutrientes(self):
        self.nutrientes -= 5 # Testeo simple de modificación de nutrientes
        print (self.nutrientes)

    def difundir_nutrientes(self):
        pass

    def aplicar_ambiente(self):
        pass

class Colonia:
    def __init__(self, ambiente):
        self.bacterias = []
        self.ambiente = ambiente

    def ubicar_hija(self, madre_fila, madre_col, hija): # Ubica a hija en la grilla
        grilla = self.ambiente.grilla
        direcciones = [     # Direcciones posibles para ubicar la hija
            (-1,0), (1,0), (0,-1), (0,1), # Verticales y horizontales
            (-1,-1), (-1,1), (1,-1), (1,1)  # Diagonales
        ]
        random.shuffle(direcciones)  # Orden aleatorio
    
        for mf, mc in direcciones: # Recorre las direcciones aleatorias
            nueva_fila = madre_fila + mf # Nueva fila basada en la dirección
            nueva_col = madre_col + mc # Nueva columna basada en la dirección
        
            # Verifica si la nueva posición está dentro de los límites de la grilla
            if 0 <= nueva_fila < grilla.shape[0] and 0 <= nueva_col < grilla.shape[1]:
                if grilla[nueva_fila, nueva_col] is None: # Verifica si la celda está vacía
                    grilla[nueva_fila, nueva_col] = hija 
                    return True  # Ubicada con éxito
        return False  # No se pudo ubicar

    def paso():
        pass

    def reporte_estado():
        pass

    def exportar_csv():
        pass