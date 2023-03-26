usuarios = [
    ["Pops", 4],
    ["Earl", 2],
    ["Alan", 3]
]
#Transformar
#nombres = [usuario[0] for usuario in usuarios]

#Filtrar
#nombres = [usuario for usuario in usuarios if usuario[1]  > 2]


#nombres = [usuario for usuario in usuarios if usuario[1]  > 3]


#nombres = list(map(lambda usuario: usuario[0], usuarios))


menosUsuarios = list(filter(lambda usuario: usuario[1] >  2, usuarios ))
print(menosUsuarios)


