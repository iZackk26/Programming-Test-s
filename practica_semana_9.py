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




