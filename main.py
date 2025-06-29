from bacteria import Bacteria
from ambiente import Ambiente
import numpy as np

def grilla_puntos(grilla): # grilla más clara con puntos
    for fila in grilla:
        for objeto in fila:
            if isinstance(objeto, Bacteria):
                print("BR" if objeto.resistente else "B", end=" ")
            else:
                print(".", end=" ") # Espacios vacios con punto
        print()

# Bacteria no resistente
bacteria1 = Bacteria( 
    id="bact-1",
    raza="E. coli",
    energia=50,
    resistente=False,
    estado="activa"
)

# Bacteria resistente
bacteria2 = Bacteria(
    id="bact-2",
    raza="Salmonella",
    energia=30,
    resistente=True,
    estado="activa"
)

ambiente = Ambiente(filas=5, columnas=5)

ambiente.grilla[0][0] = bacteria1
ambiente.grilla[1][1] = bacteria2

print("Estado inicial de la grilla:")
grilla_puntos(ambiente.grilla)