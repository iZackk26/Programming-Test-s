# Document

def sucesion(lista):
    count = 1
    for element in lista:
        result = (count + 1) / count
        if element != result:
            return False
        count += 1
    return True


def sucesion_answer():
    count = 1
    lista = []
    result = 0
    while result < 2:
        result = (count + 1) / count
        lista.append(result)
    return lista
print(sucesion_answer())
