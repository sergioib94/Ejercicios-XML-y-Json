import json

def Listar(doc):
    titulos = []
    year = []
    duracion = []
    for nombre in doc ["title"]:
        titulos.append (nombre)
    for año in doc ["year"]:
        year.append (año)
    for tiempo in doc ["duration"]:
        tiempo.append (tiempo)
    return zip (titulos,year,tiempo)


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
            for titulos ,year ,tiempo in Lista (doc):
                print ("*",titulo,"-",year, "-",tiempo)
