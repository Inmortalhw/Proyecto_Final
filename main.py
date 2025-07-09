import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from bacteria import Bacteria
from ambiente import Ambiente, Colonia
import random

# Configuración inicial
def crear_ambiente_con_bacterias(filas=5, columnas=5, num_bacterias=3):
    ambiente = Ambiente(filas, columnas)
    
    # Agregar bacterias aleatorias
    for i in range(num_bacterias):
        fila, col = random.randint(0, filas-1), random.randint(0, columnas-1)
        while ambiente.grilla[fila, col] is not None:  # Buscar posición vacía
            fila, col = random.randint(0, filas-1), random.randint(0, columnas-1)
        
        resistencia = random.random() < 0.02  # 2% de probabilidad de ser resistente
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


def plot_grilla_completa(ambiente):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    # Grilla de bacterias y antibióticos
    plot_matrix = np.zeros(ambiente.grilla.shape)
    for fila in range(ambiente.grilla.shape[0]):
        for col in range(ambiente.grilla.shape[1]):
            objeto = ambiente.grilla[fila, col]
            if objeto is not None and isinstance(objeto, Bacteria):
                if objeto.estado == "muerta":
                    plot_matrix[fila, col] = 4  # Gris
                elif objeto.consumo_reducido:  # Prioridad a consumo reducido
                    plot_matrix[fila, col] = 3  # Amarillo
                elif objeto.resistente:
                    plot_matrix[fila, col] = 2  # Rojo
                else:
                    plot_matrix[fila, col] = 1   # Verde
            elif ambiente.zona_antibiotica[fila, col]:
                plot_matrix[fila, col] = 5  # Azul
            else:
                plot_matrix[fila, col] = 0  # Blanco
    
    # Mapa de colores para bacterias
    cmap_bacterias = mcolors.ListedColormap(['white', 'green', 'red', 'yellow', 'gray', 'blue'])
    norm_bacterias = mcolors.BoundaryNorm([0, 1, 2, 3, 4, 5, 6], cmap_bacterias.N)
    
    img1 = ax1.imshow(plot_matrix, cmap=cmap_bacterias, norm=norm_bacterias)
    ax1.set_title("Bacterias y Antibióticos")
    
    # Grilla de nutrientes
    nutrientes_norm = ambiente.nutrientes / np.max(ambiente.nutrientes)  # Normalizar
    cmap_nutrientes = plt.cm.Greens
    img2 = ax2.imshow(ambiente.nutrientes, cmap=cmap_nutrientes)
    plt.colorbar(img2, ax=ax2, label='Nivel de nutrientes')
    ax2.set_title("Distribución de Nutrientes")
    
    # Configuración común
    for ax in [ax1, ax2]:
        ax.set_xticks(np.arange(-.5, ambiente.grilla.shape[1], 1), minor=True)
        ax.set_yticks(np.arange(-.5, ambiente.grilla.shape[0], 1), minor=True)
        ax.grid(which="minor", color="black", linestyle='-', linewidth=0.5)
        ax.tick_params(which="minor", size=0)
    
    # Leyendas para bacterias
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
    ax1.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    plt.show()

def simulacion_completa(filas=10, columnas=10, num_bacterias=10, pasos=5):
    # Configuración inicial
    ambiente = crear_ambiente_con_bacterias(filas, columnas, num_bacterias)
    colonia = Colonia(ambiente)
    
    print("=== Estado Inicial ===")
    plot_grilla_completa(ambiente)

    metricas = {
        'total_bacterias': [],
        'consumo_reducido': [],
        'resistentes': [],
        'nutrientes_promedio': [],
        'mutaciones': 0
    }

    for paso in range(pasos):
        # Ejecutar todos los procesos
        colonia.paso()
        ambiente.difundir_nutrientes()
        
        bacterias = [b for b in ambiente.grilla.flatten() if isinstance(b, Bacteria)]
        metricas['total_bacterias'].append(len(bacterias))
        metricas['consumo_reducido'].append(sum(b.consumo_reducido for b in bacterias))
        metricas['resistentes'].append(sum(b.resistente for b in bacterias))
        metricas['nutrientes_promedio'].append(np.mean(ambiente.nutrientes))
        
        plot_grilla_completa(ambiente)

        print(f"\n=== Paso {paso+1} ===")
        print(f"Bacterias totales: {sum(1 for x in ambiente.grilla.flatten() if isinstance(x, Bacteria))}")
        print(f"Bacterias con consumo reducido: {sum(1 for x in ambiente.grilla.flatten() if isinstance(x, Bacteria) and x.consumo_reducido)}")
        print(f"Bacterias resistentes: {sum(1 for x in ambiente.grilla.flatten() if isinstance(x, Bacteria) and x.resistente)}")
        print(f"Nutrientes promedio: {np.mean(ambiente.nutrientes):.1f}")
        
        plot_grilla_completa(ambiente)
    
    print("\n=== Simulación completada ===")
    print("\n=== Resumen Final ===")
    print(f"Mutaciones ocurridas: {metricas['mutaciones']}")
    print(f"Máximo consumo reducido: {max(metricas['consumo_reducido'])}")
    
    # Gráfico de evolución
    plt.figure(figsize=(10, 5))
    plt.plot(metricas['total_bacterias'], label='Total bacterias')
    plt.plot(metricas['consumo_reducido'], label='Consumo reducido')
    plt.plot(metricas['resistentes'], label='Resistentes')
    plt.xlabel('Pasos')
    plt.ylabel('Cantidad')
    plt.legend()
    plt.title('Evolución de la Población Bacteriana')
    plt.show()

if __name__ == "__main__":
    # Parámetros personalizables
    TAMAÑO_GRILLA = (10, 10)
    BACTERIAS_INICIALES = 20
    PASOS_SIMULACION = 5
    probabilidad_mutacion = 0.10

    # Ejecutar simulación
    simulacion_completa(
        filas=TAMAÑO_GRILLA[0],
        columnas=TAMAÑO_GRILLA[1],
        num_bacterias=BACTERIAS_INICIALES,
        pasos=PASOS_SIMULACION
    )