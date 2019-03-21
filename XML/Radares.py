def Listar (doc):
    lista = doc.xpath ('//NOMBRE/text()')
    return lista

def Contar (doc):
    radares = doc.xpath ('//CARRETERA/DENOMINACION/text()')
    return len(radares)

def Filtrar (prov,doc):
    prov = doc.xpath ('//PROVINCIA[NOMBRE="%s"]/./CARRETERA/DENOMINACION/text()' %prov)
    return (list(set(prov)))

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
        for prov in Filtrar (prov,doc):
            print ("*",prov)

    elif opcion == "0":
        break;

    else:
        print ("ERROR, esa opcion no existe")
