# Document

def sucesion(lista):
    count = 1
    for element in lista:
        result = (count + 1) / count
        if element != result:
            return False
        count += 1
    return True
#La solucion matematica se basa en crear una formula en donde se hara el (n + 1) / n, y se compara con el numero de la lista, si son iguales continua hasta terminar el ciclo

def sucesion_answer():
    count = 1
    lista = []
    result = 0
    while len(lista) < 20:
        result = (count + 1) / count
        lista.append(result)
        count += 1
    return lista
print(sucesion_answer())


# Ejercicio #3

l1 = [[7,7,7 333, 4],[20, 3, 42, 22, 12, 1, 12],[34, 34, 5,12],[45],
      [34, 5, 15]]

def aplanar(lista):
    newl = []
    for sub in lista:
        for e in sub:
            newl.append(e)
    return newl

def particionate(list):
    max = list()
    min = list()
    pivot = list[-1]
    for x in lista[:-1]:
        if x < pivote:
            min.append(x)
        else:
            max.append(x)

    return([min,pivot, max])


