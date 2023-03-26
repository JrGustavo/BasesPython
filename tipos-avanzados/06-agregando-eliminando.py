mascotas = ["Wolfgang", "Pelusa", "Wolfgang ", "Pulga", "Felipè", "Mantecada"]

mascotas.insert(-1, "Melvin")
mascotas.append("Chanchito feliz")


mascotas.remove("Pulga")
mascotas.pop(1)
del mascotas[0]
mascotas.clear()

print(mascotas)