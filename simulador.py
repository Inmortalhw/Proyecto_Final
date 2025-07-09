import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from ambiente import Ambiente
from bacteria import Bacteria

class Simulador:
    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.metricas = {
            'total_bacterias': [],
            'consumo_reducido': [],
            'resistentes': [],
            'nutrientes_promedio': [],
            'mutaciones': 0
        }

    def plot_grilla_completa(self):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        
        # Grilla de bacterias y antibióticos
        plot_matrix = np.zeros(self.ambiente.grilla.shape)
        for fila in range(self.ambiente.grilla.shape[0]):
            for col in range(self.ambiente.grilla.shape[1]):
                objeto = self.ambiente.grilla[fila, col]
                if objeto is not None and isinstance(objeto, Bacteria):
                    if objeto.estado == "muerta":
                        plot_matrix[fila, col] = 4  # Gris
                    elif objeto.consumo_reducido:
                        plot_matrix[fila, col] = 3  # Amarillo
                    elif objeto.resistente:
                        plot_matrix[fila, col] = 2  # Rojo
                    else:
                        plot_matrix[fila, col] = 1   # Verde
                elif self.ambiente.zona_antibiotica[fila, col]:
                    plot_matrix[fila, col] = 5  # Azul
                else:
                    plot_matrix[fila, col] = 0  # Blanco
        
        # Mapa de colores para bacterias
        cmap_bacterias = mcolors.ListedColormap(['white', 'green', 'red', 'yellow', 'gray', 'blue'])
        norm_bacterias = mcolors.BoundaryNorm([0, 1, 2, 3, 4, 5, 6], cmap_bacterias.N)
        
        img1 = ax1.imshow(plot_matrix, cmap=cmap_bacterias, norm=norm_bacterias)
        ax1.set_title("Bacterias y Antibióticos")
        
        # Grilla de nutrientes
        nutrientes_norm = self.ambiente.nutrientes / np.max(self.ambiente.nutrientes + 1e-10)  # Evita división por cero
        cmap_nutrientes = plt.cm.Greens
        img2 = ax2.imshow(self.ambiente.nutrientes, cmap=cmap_nutrientes)
        plt.colorbar(img2, ax=ax2, label='Nivel de nutrientes')
        ax2.set_title("Distribución de Nutrientes")
        
        # Configuración común
        for ax in [ax1, ax2]:
            ax.set_xticks(np.arange(-.5, self.ambiente.grilla.shape[1], 1), minor=True)
            ax.set_yticks(np.arange(-.5, self.ambiente.grilla.shape[0], 1), minor=True)
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

    def graficar_evolucion(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.metricas['total_bacterias'], label='Total bacterias')
        plt.plot(self.metricas['consumo_reducido'], label='Consumo reducido')
        plt.plot(self.metricas['resistentes'], label='Resistentes')
        plt.xlabel('Pasos')
        plt.ylabel('Cantidad')
        plt.legend()
        plt.title('Evolución de la Población Bacteriana')
        plt.show()

    def actualizar_metricas(self, paso):
        bacterias = [b for b in self.ambiente.grilla.flatten() if isinstance(b, Bacteria)]
        self.metricas['total_bacterias'].append(len(bacterias))
        self.metricas['consumo_reducido'].append(sum(b.consumo_reducido for b in bacterias))
        self.metricas['resistentes'].append(sum(b.resistente for b in bacterias))
        self.metricas['nutrientes_promedio'].append(np.mean(self.ambiente.nutrientes))
        
        print(f"\n=== Paso {paso+1} ===")
        print(f"Bacterias totales: {len(bacterias)}")
        print(f"Bacterias con consumo reducido: {self.metricas['consumo_reducido'][-1]}")
        print(f"Bacterias resistentes: {self.metricas['resistentes'][-1]}")
        print(f"Nutrientes promedio: {self.metricas['nutrientes_promedio'][-1]:.1f}")