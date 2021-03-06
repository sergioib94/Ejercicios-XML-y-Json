import json

def Lista(doc):
    for datos in doc:
        print ("titulo:",datos ["title"],end="")
        print (" -", datos ["year"],end="")
        print (" -", datos ["duration"], " ",end="")
        print ("")

def Contar(doc):
    for datos in doc:
        print ("titulos:",datos ["title"])
        print ("La pelicula tiene %d actores: " %(len(datos ["actors"])))
        print ("")

def Filtrar (palabra1,palabra2,doc):
    pelicula = []
    for datos in doc:
        if palabra1 and palabra2 in datos ["storyline"]:
            pelicula.append (datos ["title"])
    return pelicula

def Buscar (nombre,doc):
    pelicula = []
    for datos in doc:
        for actor in datos ["actors"]:
            if actor == nombre:
                pelicula.append (datos["title"])
    return pelicula

with open("movies.json") as fichero:
    doc = json.load(fichero)

while True:
    print ('''Menu:
        1. Listar información: Listar el título, año y duración de todas las películas..
        2. Contar información: Mostrar los títulos de las películas y el número de actores/actrices que tiene cada una.
        3. Filtrar información: Mostrar las películas que contengan en la sinopsis dos palabras dadas.
        4. Buscar información relacionada: Mostrar las películas en las que ha trabajado un actor dado.
        5. Ejercicio libre: Mostrar el título y la url del póster de las tres películas con una media de puntuaciones más alta y lanzadas entre dos fechas dadas.
        0. Salir
        ''')

    opcion = input("opcion: ")

    if opcion == "1":
        Lista (doc)

    elif opcion == "2":
        Contar(doc)

    elif opcion == "3":
        palabra1 = input("palabra1: ")
        palabra2 = input("palabra2: ")
        if len(Filtrar(palabra1,palabra2,doc)) == 1:
            print ("Estas palabras aparecen en la sinopsis de %s" %(Filtrar(palabra1,palabra2,doc)))

        elif len(Filtrar(palabra1,palabra2,doc)) > 1:
            print ("Estas palabras aparecen en:")
            print ("*", Filtrar(palabra1,palabra2,doc))
            
        else:
            print ("Estas palabras no aparecen en ninguna sinopsis")

    elif opcion == "4":
        nombre = input("Nombre del actor: ")
        for titulo in Buscar(nombre,doc):
            print ("*",titulo)

    elif opcion == "0":
        break;
