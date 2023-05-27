#Ejercicios de Practica de Examen:

#Ejercicio semana 9, similares a un examen:

def succesion(lista):
    """This function says if the element is equal to the succesion
    Args:
        lista {list} -- List with the elements to iterate
    Returns:
        True or False, depending if the element fullfill the succesion
    """
    c = 1
    for element in lista:
        result = (c + 1) / c
        if element != result:
            return False
        c += 1
    return True


#Ejercicio semana 9, #3, similar a un examen:

#Parte A

def plain(lista):
    new_list = []
    for element in lista:
        new_list.extend(element)
    return new_list

#Parte B

def quick_sort(lista):
    lenght = len(lista)
    if lenght <= 1:
        return lista
    else:
        pivot = lista.pop()
    big = []
    small = []
    for element in lista:
        if element < pivot:
            small.append(element)
        else:
            big.append(element)
    return quick_sort(small) + [pivot] + quick_sort(big)

#Parte C

def two_repeated(lista):
    new_list = []
    for element in lista:
        repeat = new_list.count(element)
        if repeat < 2:
            new_list.append(element)
    return new_list

#Parte D


def particionate(lista):
    end = []
    for element in range(0,len(lista),5):
        end.append(lista[element: element + 5])
    return end








def groups(lista):
    final = []
    for x in range(0, len(lista), 5):
        final.append(lista[x:x + 5])
    return final


