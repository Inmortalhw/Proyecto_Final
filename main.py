import random
from bacteria import Bacteria
from ambiente import Ambiente, Colonia
from simulador import Simulador

def crear_ambiente_con_bacterias(filas=5, columnas=5, num_bacterias=3):
    ambiente = Ambiente(filas, columnas)
    
    for i in range(num_bacterias):
        fila, col = random.randint(0, filas-1), random.randint(0, columnas-1)
        while ambiente.grilla[fila, col] is not None:
            fila, col = random.randint(0, filas-1), random.randint(0, columnas-1)
        
        resistencia = random.random() < 0.02
        ambiente.grilla[fila, col] = Bacteria(
            id=f"B{i}",
            raza="cilobac",
            energia=random.randint(40, 60),
            resistente=resistencia
        )
    
    centro_fila, centro_col = filas//2, columnas//2
    ambiente.agregar_zona_antibiotica(fila=centro_fila, col=centro_col, radio=1)
    
    return ambiente

def ejecutar_simulacion(filas=10, columnas=10, num_bacterias=10, pasos=5, archivo_salida="simulacion_log.txt"):
    ambiente = crear_ambiente_con_bacterias(filas, columnas, num_bacterias)
    colonia = Colonia(ambiente)
    simulador = Simulador(ambiente, archivo_salida)
    
    simulador.escribir_log("=== Estado Inicial ===")
    simulador.plot_grilla_completa()

    for paso in range(pasos):
        colonia.paso()
        simulador.actualizar_metricas(paso)
        simulador.plot_grilla_completa()
    
    simulador.finalizar_simulacion()
    simulador.graficar_evolucion()

if __name__ == "__main__":
    # Parámetros configurables
    TAMAÑO_GRILLA = (10, 10)
    BACTERIAS_INICIALES = 20
    PASOS_SIMULACION = 5
    
    ejecutar_simulacion(
        filas=TAMAÑO_GRILLA[0],
        columnas=TAMAÑO_GRILLA[1],
        num_bacterias=BACTERIAS_INICIALES,
        pasos=PASOS_SIMULACION
    )