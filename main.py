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
                elif hasattr(Bacteria, 'consumo_reducido'):
                    print("BC", end=" ")
                else:
                    print("B", end=" ")
            elif zona_antibiotica[fila, col]:
                print("A", end=" ") # Antibióticos con A
            else:
                print(".", end=" ") # Espacios vacios con punto
        print()

# Crear ambiente
ambiente = Ambiente(filas=5, columnas=5)

# Agregar bacterias
bacteria_normal = Bacteria(id="B1", raza="Salmonela", resistente=False, estado="activa")
bacteria_resistente = Bacteria(id="B2", raza="Cilobacter", resistente=True, estado="activa")
ambiente.grilla[2, 2] = bacteria_normal
ambiente.grilla[2, 3] = bacteria_resistente

# Crear zona antibiótica (centro de 3x3)
ambiente.agregar_zona_antibiotica(2, 2, radio=1)

# Mostrar grilla
print("Antes del paso:")
grilla_puntos(ambiente.grilla, ambiente.zona_antibiotica)

# Ejecutar paso de simulación
colonia = Colonia(ambiente)
colonia.paso()

print("\nDespués del paso:")
grilla_puntos(ambiente.grilla, ambiente.zona_antibiotica)