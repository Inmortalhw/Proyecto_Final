from bacteria import Bacteria

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