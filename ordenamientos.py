#Ordenamiento por Insercion

def big(lista):
    x = lista[-1]
    for element in lista:
        if element > x:
            x = element
    return x

def insertion_sort(lista):
    data = []
    while len(lista) > 0:
        bigg = big(lista)
        data.append(bigg)
        lista.remove(bigg)
    return data



# Ordenamiento de Burbuja

def bubble_sort(lista):
    x = len(lista)- 1
    while x > 0:
        i = 0
        while i < x:
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
            i += 1
        x -= 1
    return lista



#Ordenamiento Quicksort

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
    return quick_sort(big) + [pivot] + quick_sort(small)

lista = [7,8,9,1,2,3,6,5,4,2,6,8,9,10]

# print(quick_sort(lista))

#Esta es la funcion base, se puede modificar con la funcion max, para poder llegar reducir la funcion a una unica

# def bigger(lista):
#     big = lista[-1]
#     for element in lista:
#         if element > big:
#             big = element
#     return big


# def insertion_sorty(lista):
#     data = []
#     while len(lista) > 0:
#         biggy = big(lista)
#         data.append(biggy)
#         lista.remove(biggy)
#     return data

def insertion_sorty(lista):
    data = []
    while len(lista) > 0:
        big = max(lista)
        data.append(big)
        lista.remove(big)
    return data



print(insertion_sorty(lista))



