# Insertion sorted
def insertion_sort(lista):
    data = []
    while len(lista) > 0:
        x = max(lista)
        data.append(x)
        lista.remove(x)
    return data


# print(insertion_sort(x))


def bubble_sort(lista):
    vueltas = len(lista)-1
    while vueltas > 0:
        repeat = 0
        while repeat < vueltas:
            if lista[repeat] < lista[repeat + 1]:
                lista[repeat], lista[repeat + 1] = lista[repeat + 1], lista[repeat]
            repeat += 1
        vueltas -= 1
    return lista

# print(bubble_sort(x))

def quick_sort(lista):
    if len(lista) <= 1:
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

x = [1,2,3,4,5,6,7,8,9]



print(quick_sort(x))
