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
# print(sucesion_answer())


# Ejercicio #3

def ordenamiento_quickSort(lista):
    if len(lista)>0:
        lista=particiona_lista(lista)
        cont=0
        while cont<len(lista):
            e=lista[cont]
            if type(e)==list:
                if len(e)==0:
                    del lista[cont]
                elif len(e)==1:
                    lista[cont]=e[0]
                    cont = cont + 1
                else:
                    lista=lista[:cont]+particiona_lista(e)+lista[cont+1:]
            else:
                cont=cont+1
            
    return lista


def particiona_lista(lista):
    menores=list()
    mayores=list()
    pivote=lista[-1]
    for x in lista[:-1]:
        if x<pivote:
            menores.append(x)
        else:
            mayores.append(x) 
    return([menores,pivote,mayores])

def aplanar(lista):
    newl = []
    for sub in lista:
        if type(sub) == list:
            newl.extend(aplanar(sub))
        else:
            newl.append(sub)
    return newl

def repeated(lista):
    new_list = []
    second_list = []
    i = 0
    for element in lista:
        if element not in new_list:
            new_list.append(element)
        elif element in new_list and element not in second_list:
            second_list.append(element)
    for element in second_list:
        index = new_list.index(element)
        new_list.insert(index, element)
    return new_list
            

        


# lista = [[7,7,7,333,4],[20,3,42,22,12,1,12],[34,34,5,12],[45],[34,5,15]]
lista = [1,3,4,55,777,12,12,12,15,20,22,34,34,34,42,45,333]
new_list = aplanar(particiona_lista(lista))
new_2_list = repeated(lista)
# print(new_2_list)


def sublists(list):
    salida = []
    for n in range(0,len(lista),5):
        salida.append(lista[n:n + 5])
    return salida

print(sublists(new_2_list))
