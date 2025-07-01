from bacteria import Bacteria
from ambiente import Ambiente, Colonia
import numpy as np

def grilla_puntos(grilla): # Grilla con puntos
    for fila in grilla:
        for objeto in fila:
            if isinstance(objeto, Bacteria):
                if objeto.estado == "muerta":
                    print("X", end=" ") # Bacterias muertas con X
                elif objeto.resistente:
                    print("BR", end=" ") # Bacterias resistentes con BR
                elif hasattr(objeto, 'consumo_reducido'): # Verifica si tiene mutación perjudicial
                    print("BC", end=" ") # Bacterias con mutación perjudicial con BC
                else:
                    print("B", end=" ") # Bacterias normales con B
            else:
                print(".", end=" ") # Espacios vacios con punto
        print()

# 1. Crear ambiente y poner nutrientes desiguales
ambiente = Ambiente(filas=5, columnas=5)
ambiente.nutrientes[0,0] = 60  # Muchos nutrientes aquí
ambiente.nutrientes[0,1] = 20  # Pocos nutrientes aquí
ambiente.nutrientes[4,0] = 10  # Muy pocos nutrientes aquí
ambiente.nutrientes[4,4] = 0  # Sin nutrientes aquí

# Mostrar antes
print("ANTES:")
print(ambiente.nutrientes)

# Aplicar difusión
ambiente.difundir_nutrientes()

# Mostrar después
print("\nDESPUÉS:")
print(ambiente.nutrientes)

# Segunda difusión para ver equilibrio
ambiente.difundir_nutrientes()

# Mostrar después de la segunda difusión
print("\nGrilla de nutrientes después de la segunda difusión:")
print(ambiente.nutrientes)
