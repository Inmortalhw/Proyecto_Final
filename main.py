import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from bacteria import Bacteria
from ambiente import Ambiente, Colonia

# Configuración inicial
def crear_ambiente_con_bacterias(filas=5, columnas=5, num_bacterias=3):
    ambiente = Ambiente(filas, columnas)
    
    # Agregar bacterias aleatorias
    for i in range(num_bacterias):
        fila, col = random.randint(0, filas-1), random.randint(0, columnas-1)
        while ambiente.grilla[fila, col] is not None:  # Buscar posición vacía
            fila, col = random.randint(0, filas-1), random.randint(0, columnas-1)
        
        resistencia = random.random() < 0.2  # 20% de probabilidad de ser resistente
        ambiente.grilla[fila, col] = Bacteria(
            id=f"B{i}",
            raza="cilobac",
            energia=random.randint(40, 60),
            resistente=resistencia
        )
    
    # Agregar zona antibiótica central
    centro_fila, centro_col = filas//2, columnas//2
    ambiente.agregar_zona_antibiotica(fila=centro_fila, col=centro_col, radio=1)
    
    return ambiente


def plot_grilla(grilla, zona_antibiotica):
    # Crear un mapa de colores personalizado
    cmap = mcolors.ListedColormap(['white', 'green', 'red', 'yellow', 'gray', 'blue'])
    bounds = [0, 1, 2, 3, 4, 5, 6]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)
    
    # Crear matriz numérica para matplotlib
    plot_matrix = np.zeros(grilla.shape)
    
    for fila in range(grilla.shape[0]):
        for col in range(grilla.shape[1]):
            objeto = grilla[fila, col]
            
            if objeto is not None and isinstance(objeto, Bacteria):
                if objeto.estado == "muerta":
                    plot_matrix[fila, col] = 4  # Gris para muertas
                elif objeto.resistente:
                    plot_matrix[fila, col] = 2  # Rojo para resistentes
                elif hasattr(objeto, 'consumo_reducido'):
                    plot_matrix[fila, col] = 3  # Amarillo para consumo reducido
                else:
                    plot_matrix[fila, col] = 1  # Verde para normales
            elif zona_antibiotica[fila, col]:
                plot_matrix[fila, col] = 5  # Azul para antibióticos
            else:
                plot_matrix[fila, col] = 0  # Blanco para vacío
    
    # Configurar el gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    img = ax.imshow(plot_matrix, cmap=cmap, norm=norm)
    
    # Crear leyenda
    legend_labels = {
        'Vacío': 'white',
        'Bacteria normal': 'green',
        'Bacteria resistente': 'red',
        'Bacteria consumo reducido': 'yellow',
        'Bacteria muerta': 'gray',
        'Antibiótico': 'blue'
    }
    patches = [plt.plot([], [], marker="s", ms=10, ls="", 
                        color=color, label=label)[0] 
               for label, color in legend_labels.items()]
    ax.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Añadir líneas de la grilla
    ax.set_xticks(np.arange(-.5, grilla.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-.5, grilla.shape[0], 1), minor=True)
    ax.grid(which="minor", color="black", linestyle='-', linewidth=0.5)
    ax.tick_params(which="minor", size=0)
    
    # Mostrar valores en las celdas
    for i in range(grilla.shape[0]):
        for j in range(grilla.shape[1]):
            if plot_matrix[i, j] > 0:
                ax.text(j, i, int(plot_matrix[i, j]), 
                        ha="center", va="center", color="black")
    
    plt.title("Simulación de Colonias Bacterianas")
    plt.tight_layout()
    plt.show()

def simulacion_interactiva(ambiente, pasos=5, delay=1.0):
    colonia = Colonia(ambiente)
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.ion()  # Modo interactivo
    
    cmap = mcolors.ListedColormap(['white', 'green', 'red', 'yellow', 'gray', 'blue'])
    norm = mcolors.BoundaryNorm([0, 1, 2, 3, 4, 5, 6], cmap.N)
    
    for paso in range(pasos):
        colonia.paso()
        
        # Actualizar matriz de visualización
        plot_matrix = np.zeros(ambiente.grilla.shape)
        for fila in range(ambiente.grilla.shape[0]):
            for col in range(ambiente.grilla.shape[1]):
                objeto = ambiente.grilla[fila, col]
                if objeto is not None and isinstance(objeto, Bacteria):
                    if objeto.estado == "muerta":
                        plot_matrix[fila, col] = 4
                    elif objeto.resistente:
                        plot_matrix[fila, col] = 2
                    elif hasattr(objeto, 'consumo_reducido'):
                        plot_matrix[fila, col] = 3
                    else:
                        plot_matrix[fila, col] = 1
                elif ambiente.zona_antibiotica[fila, col]:
                    plot_matrix[fila, col] = 5
                else:
                    plot_matrix[fila, col] = 0
        
        ax.clear()
        ax.imshow(plot_matrix, cmap=cmap, norm=norm)
        
        # Añadir líneas de la grilla
        ax.set_xticks(np.arange(-.5, ambiente.grilla.shape[1], 1), minor=True)
        ax.set_yticks(np.arange(-.5, ambiente.grilla.shape[0], 1), minor=True)
        ax.grid(which="minor", color="black", linestyle='-', linewidth=0.5)
        ax.tick_params(which="minor", size=0)
        
        ax.set_title(f"Paso {paso+1}")
        plt.draw()
        plt.pause(delay)
    
    plt.ioff()
    plt.show()

# Crear ambiente y configurar simulación
ambiente = Ambiente(filas=10, columnas=10)
bacteria = Bacteria(id="B1", raza="cilobac", energia=65, resistente=True)
ambiente.grilla[0,0] = bacteria
ambiente.agregar_zona_antibiotica(fila=2, col=2, radio=1)

# Visualización paso a paso
print("Estado inicial:")
plot_grilla(ambiente.grilla, ambiente.zona_antibiotica)

colonia = Colonia(ambiente)
colonia.paso()
print("\nDespués del primer paso:")
plot_grilla(ambiente.grilla, ambiente.zona_antibiotica)

colonia.paso()
print("\nDespués del segundo paso:")
plot_grilla(ambiente.grilla, ambiente.zona_antibiotica)

# Simulación interactiva reversa
print("\nSimulación interactiva:")
simulacion_interactiva(ambiente, pasos=3, delay=1.0)