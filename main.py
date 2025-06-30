from bacteria import Bacteria
from ambiente import Ambiente, Colonia
import numpy as np

def grilla_puntos(grilla): # Grilla con puntos
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
colonia = Colonia(ambiente)

ambiente.grilla[0, 0] = bacteria1
ambiente.grilla[1, 2] = bacteria2

print("Estado inicial de la grilla:")
grilla_puntos(ambiente.grilla)

bacteria2.morir() # Bacteria2 muere por falta de energía

# Bacteria1 se divide:
hija = bacteria1.dividirse(probabilidad_mutacion=1)

if hija:
    # Obtener posición de la madre
    madre_fila, madre_col = 0, 0  # Posición de bacteria1 en la grilla
    
    if colonia.ubicar_hija(madre_fila, madre_col, hija):
        print(f"Bacteria hija {hija.id} ha sido ubicada en la grilla, resistente: {hija.resistente}")
    else:
        print("No había espacio para dividirse.")

print("Estado final de la grilla:")
grilla_puntos(ambiente.grilla)

print(f"\nenergia de bacteria1: {bacteria1.energia}, energia de nueva_bacteria: {hija.energia if hija else 'N/A'}")