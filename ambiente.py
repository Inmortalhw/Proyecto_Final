import numpy as np #importación de numpy para comenzar grilla

class Ambiente:
    def __init__(self, filas, columnas):
        self.grilla = np.zeros((filas, columnas), dtype=object) #Grilla de tipo objetos sin nada
        self.nutrientes = np.full((filas, columnas), 40) #Grilla de nutrientes con valor 40
        self.factores = {
            "antibióticos": None
        }

    def actualizar_nutrientes(self):
        self.nutrientes -= 5 # Testeo simple de modificación de nutrientes
        print (self.nutrientes)

    def difundir_nutrientes(self):
        pass

    def aplicar_ambiente(self):
        pass

class Colonia:
    def __init__(self, ambiente):
        self.bacterias = []
        self.ambiente = ambiente

    def paso():
        pass

    def reporte_estado():
        pass

    def exportar_csv():
        pass