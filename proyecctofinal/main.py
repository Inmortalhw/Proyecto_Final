from bacteria import Bacteria
from ambiente import Ambiente

bacteria1 = Bacteria(
    id="bact-1",
    raza="E. coli",
    energia=50,
    resistente=False,
    estado="activa"
)

print(f"Bacteria ID: {bacteria1.id}")
print(f"Bacteria Raza: {bacteria1.raza}")
print(f"Bacteria Energía: {bacteria1.energia}")
print(f"Bacteria Resistente: {bacteria1.resistente}")
print(f"Bacteria Estado: {bacteria1.estado}")

#Grilla base del ambiente 
ambiente = Ambiente(filas=5, columnas=5)

#Grilla vacia
print("grilla inicial")
print(ambiente.grilla)

#Grilla de nutrientes
print("nutrientes iniciales")
print(ambiente.nutrientes)

#Modificación de nutrientes
print("actualización de nutrientes")
ambiente.actualizar_nutrientes()

# Simulación de un paso (solo para mostrar el funcionamiento de grilla y nutrientes)
print("\n=== SIMULANDO UN PASO ===")

ambiente.grilla[0, 0] = bacteria1
print("\nBacteria colocada en (0,0):")
print(ambiente.grilla)

consumo = bacteria1.alimentar(ambiente.nutrientes[0, 0])
ambiente.nutrientes[0, 0] -= consumo

print("\nNutrientes después de alimentarse:")
print(ambiente.nutrientes)

print("\nActualizando nutrientes en todo el ambiente:")
ambiente.actualizar_nutrientes()