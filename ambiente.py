import numpy as np # Importación de numpy para manejar la grilla y nutrientes
from bacteria import Bacteria #importación de la clase Bacteria
import random

class Ambiente:
    def __init__(self, filas, columnas):
        self.grilla = np.full((filas, columnas), None, dtype=object) #Grilla de tipo objetos sin nada
        self.nutrientes = np.full((filas, columnas), 50) #Grilla de nutrientes con valor 40
        self.zona_antibiotica = np.zeros((filas, columnas), dtype=bool) # Grilla de tipo booleana de antibioticos

    def actualizar_nutrientes(self):
        self.nutrientes -= 5 # Testeo simple de modificación de nutrientes
        print (self.nutrientes)
        self.nutrientes[self.nutrientes < 0] = 0  # Evita que los nutrientes sean negativos

    def difundir_nutrientes(self):
        # Copia los nutrientes actuales, así no modificamos el original durante la difusión
        nuevos_nutrientes = self.nutrientes.copy()
    
        # Recorre todas las celdas
        for fila in range(self.nutrientes.shape[0]):
            for col in range(self.nutrientes.shape[1]):

                    # Coordenadas de las celdas vecinas
                    vecinos = [] # Lista para almacenar los nutrientes de las celdas vecinas
                    for df, dc in [(-1,0), (1,0), (0,-1), (0,1)]:  # Arriba, abajo, izquierda, derecha
                        nf = fila + df # Movimiento en fila (nueva fila)
                        nc = col + dc  # Movimiento en columna (nueva columna)
                        # Verifica que nf y nc están dentro de los límites de la grilla
                        if 0 <= nf < self.nutrientes.shape[0] and 0 <= nc < self.nutrientes.shape[1]:
                            vecinos.append(self.nutrientes[nf, nc]) # Añade el valor de nutrientes de la celda vecina a la lista
                
                    if vecinos:  # Si tiene vecinos
                    # Suma los nutrientes de las celdas vecinas y las divide por la cantidad de vecinos
                        promedio = sum(vecinos) / len(vecinos)
                        # Actualiza el valor de nutrientes de la celda actual sumando el promedio
                        # con un factor de 0.5 para suavizar la difusión
                        nuevos_nutrientes[fila, col] = 0.5 * self.nutrientes[fila, col] + 0.5 * promedio  # Actualizar
    
        # Aplicar cambios
        self.nutrientes = nuevos_nutrientes

    # Agrega una zona antibiótica en la grilla
    def agregar_zona_antibiotica(self, fila, col, radio=1):
        for i in range(max(0, fila - radio), min(fila + radio + 1, self.zona_antibiotica.shape[0])):
            for j in range(max(0, col - radio), min(col + radio + 1, self.zona_antibiotica.shape[1])):
                self.zona_antibiotica[i, j] = True
    
    def eliminar_zona_antibiotica(self, fila, columna):
        self.zona_antibiotica.fill(False)  # Elimina todas las zonas antibióticas

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

    def paso(self):
        # Primero: Difundir nutrientes
        self.ambiente.difundir_nutrientes()
    
        for fila in range(self.ambiente.grilla.shape[0]):
            for col in range(self.ambiente.grilla.shape[1]):
                bacteria = self.ambiente.grilla[fila, col]
            
                if isinstance(bacteria, Bacteria):
                    # 1. Alimentarse de nutrientes disponibles
                    nutrientes_celda = self.ambiente.nutrientes[fila, col]
                    consumo = bacteria.alimentar(nutrientes_celda)
                    self.ambiente.nutrientes[fila, col] -= consumo
                
                    # 2. Consumo de energía metabólica
                    bacteria.consumir_energia()
                
                    # 3. Reproducción
                    if bacteria.energia >= 60:
                        hija = bacteria.dividirse()
                        if hija:
                            self.ubicar_hija(fila, col, hija)
                
                    # 4. Muerte
                    en_zona_antibiotica = self.ambiente.zona_antibiotica[fila, col]
                    if bacteria.morir(en_zona_antibiotica):
                        self.ambiente.grilla[fila, col] = None
    
        # Actualizar nutrientes después de todo el paso
        self.ambiente.actualizar_nutrientes()

    def reporte_estado():
        pass

    def exportar_csv():
        pass