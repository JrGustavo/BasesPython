numeros = [2, 3, 4, 5, 6, 7, 8]

numeros2 = sorted(numeros)
sorted(numeros)
print(numeros2)

usuarios = [
    ["Pops", 4],
    ["Earl", 2],
    ["Alan", 3]

]

def ordena(elemento):
    return elemento[1]

usuarios.sort(key=lambda el:el[1], reverse=True)
print(usuarios)