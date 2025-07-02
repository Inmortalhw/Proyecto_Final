from bacteria import Bacteria
from ambiente import Ambiente, Colonia
import numpy as np

def grilla_puntos(grilla, zona_antibiotica): # Grilla con puntos
    for fila in range(grilla.shape[0]):
        for col in range(grilla.shape[1]):
            objeto = grilla[fila, col]
            if objeto is not None and isinstance(objeto, Bacteria): # Verifica si hay una bacteria
                if objeto.estado == "muerta":
                    print("X", end=" ")
                elif objeto.resistente:
                    print("BR", end=" ")
                elif hasattr(objeto, 'consumo_reducido'):
                    print("BC", end=" ")
                else:
                    print("B", end=" ")
            elif zona_antibiotica[fila, col]:
                print("A", end=" ") # Antibióticos con A
            else:
                print(".", end=" ") # Espacios vacios con punto
        print()

ambiente = Ambiente(filas=5, columnas=5) # Crear ambiente de 5x5

bacteria = Bacteria(id="B1", raza="cilobac", energia=65, resistente=True)
ambiente.grilla[0,0] = bacteria

ambiente.agregar_zona_antibiotica(fila=2, col=2, radio=1) # Agregar zona antibiótica en (2,2)

grilla_puntos(ambiente.grilla, ambiente.zona_antibiotica)
print("energía de la bacteria:", bacteria.energia)

colonia = Colonia(ambiente)
colonia.paso()
print("Después del primer paso:")

grilla_puntos(ambiente.grilla, ambiente.zona_antibiotica)
print("energía de la bacteria después del paso:", bacteria.energia)

colonia.paso() # Realizar otro paso
grilla_puntos(ambiente.grilla, ambiente.zona_antibiotica)

print("energía de la bacteria después del paso:", bacteria.energia)