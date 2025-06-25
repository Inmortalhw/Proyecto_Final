class Ambiente:
    def __init__(self, grilla, nutrientes, factores):
        self.grilla = grilla
        self.nutrientes = nutrientes
        self.factores = {
            "antibióticos": None
        }

    def actualizar_nutrientes(self):
        pass

    def difundir_nutrientes(self):
        pass

    def aplicar_ambiente(self):
        pass

class Colonia:
    def __init__(self, ambiente):
        self.bacterias = []
        self.ambiente = ambiente

    def agregar_bacteria(self, bacteria):
        self.bacterias.append(bacteria)

    def eliminar_bacteria(self, bacteria):
        self.bacterias.remove(bacteria)

    def paso(self):
        nuevas_bacterias = []
        ambiente = self.ambiente
    
    def paso()
        pass

    def reporte_estado()
        pass

    def exportar_csv()
        pass