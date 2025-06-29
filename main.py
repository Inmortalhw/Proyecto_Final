from bacteria import Bacteria
from ambiente import Ambiente
import numpy as np

def grilla_puntos(grilla): # grilla más clara con puntos
    for fila in grilla:
        for objeto in fila:
            if isinstance(objeto, Bacteria):
                if objeto.estado == "muerta":
                    print("X", end=" ") # Bacterias muertas con X
                else:
                    print("BR" if objeto.resistente else "B", end=" ")
            else:
                print(".", end=" ") # Espacios vacios con punto
        print()

# Bacteria a dividir
bacteria1 = Bacteria( 
    id="bact-1",
    raza="E. coli",
    energia=80, # Energía suficiente para dividirse
    resistente=False,
    estado="activa"
)

bacteria2 = Bacteria(
    id="bact-2",
    raza="Salmonella",
    energia=5, # Energía insuficiente para sobrevivir
    resistente=True,
    estado="activa"
)

ambiente = Ambiente(filas=5, columnas=5)

ambiente.grilla[0, 0] = bacteria1
ambiente.grilla[1, 2] = bacteria2

bacteria2.morir() # Bacteria2 muere por falta de energía
nueva_bacteria = bacteria1.dividirse() # Crear una nueva bacteria
ambiente.grilla[1, 1] = nueva_bacteria

print("Estado inicial de la grilla:")
grilla_puntos(ambiente.grilla)

print(f"\nenergia de bacteria1: {bacteria1.energia}, energia de nueva_bacteria: {nueva_bacteria.energia}")