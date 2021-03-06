def Listar (doc):
    lista = doc.xpath ('//NOMBRE/text()')
    return lista

def Contar (doc):
    radares = doc.xpath ('//CARRETERA/DENOMINACION/text()')
    return len(radares)

def Filtrar (prov,doc):
    via = doc.xpath ('//PROVINCIA[NOMBRE="%s"]/./CARRETERA/DENOMINACION/text()' %prov)
    radar = int(doc.xpath ('count(//PROVINCIA[NOMBRE="%s"]/./CARRETERA/RADAR)' %prov))
    repeticion = list(set(via)) #list set evita repeticiones en la lista
    filtro = [repeticion,radar]
    return filtro

def Buscar (via,doc):
    prov = doc.xpath ('//CARRETERA[DENOMINACION="%s"]/..//NOMBRE/text()' %via)
    radarI = doc.xpath ('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/PK/text()' %via)
    radarF = doc.xpath ('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_FINAL/PK/text()' %via)
    busqueda = [prov,radarI,radarF]
    return busqueda

def Localizar (via, doc):
    cont = int(doc.xpath ('count(//CARRETERA[DENOMINACION="%s"]/RADAR)' %via))
    latitud = doc.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/LATITUD/text()' %via)
    longitud = doc.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/LONGITUD/text()' %via)

    mapa = "http://www.openstreetmap.org/#map=20/%s/%s"%(latitud[0],longitud[0])

    return mapa


from lxml import etree
doc = etree.parse ('Radares.xml')

while True:
    print ('''Menu:
        1.Listar información: Mostrar el nombre de las provincias de las que tenemos información sobre radares.
        2.Contar información: Mostrar la cantidad de radares de los que tenemos información.
        3.Buscar o filtrar información: Pedir por teclado una provincia y mostrar el nombre de las carreteras que tiene y la cantidad de radares.
        4.Buscar información relacionada: Pedir por teclado una carretera, muestra las provincias por la que pasa y sus respectivos radares.
        5.Ejercicio libre: Pedir por teclado una carretera, cuenta los radares que tiene y muestra las coordenadas de los radares.
        0.Salir''')

    opcion = input("opcion: ")

    if opcion == "1":
        for provincias in Listar (doc):
            print ("*",provincias)

    elif opcion == "2":
        print ("contamos con: %d radares" %(Contar(doc)))

    elif opcion == "3":
        prov = input ("Introduce la provincia que quieras mirar: ")
        for via in Filtrar (prov,doc)[0]:
            print ("*",via)
        print ("La provincia tiene", Filtrar (prov,doc)[1], "radares")

    elif opcion == "4":
        via = input ("Introduce la carretera que quieras mirar: ")
        for prov in Buscar (via,doc)[0]:
            print ("*",prov)
        for radarI,radarF in zip (Buscar (via,doc)[1],Buscar (via,doc)[2]):
            print (radarI,"-",radarF)

    elif opcion == "5":
        via = input("Dime el nombre de la carretera para obtener la localizacion de los radares: ")
        print (Localizar(via,doc))

    elif opcion == "0":
        break;

    else:
        print ("ERROR, esa opcion no existe")
