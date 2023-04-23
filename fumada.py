#Crear un algorítmo que reciba una lista con cuatro sublistas, donde cada sublista contiene los dígitos necesarios para realizar una contraseña

lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

def invert(lista):
    final = []
    for sublist in lista:
        final.append(sublist[::-1])
        
    return final

def extend(lista):
    final = []
    c = 0
    for sublist in lista:
        r = 0
        for element in sublist:
            r = (r * 10) + element
        final.append([r])
    return final

def explain(lista):
    final = []
    for sublist in lista:
        final.extend(sublist)
    return final

lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

x = explain(extend(lista))
def position_sum(lista):
    n = []
    even, odd = 0, 0
    for i, num in enumerate(lista):
        if i % 2 == 0:
            even += num
        else:
            odd += num
    return [even, odd]


def multiplier(lista):
    new = []
    for element in lista:
        new.append(element)
        new.append(element * 2)
    return new


def quick_sort(lista):
    lenght = len(lista)
    if lenght <= 0:
        return lista
    else:
        pivot = lista.pop()
    small = []
    big = []
    for element in lista:
        if element < pivot:
            small.append(element)
        else:
            big.append(element)
    return quick_sort(small) + [pivot] + quick_sort(big)

y = position_sum(x)
z = multiplier(y)
print(quick_sort(z))
