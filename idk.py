# Retornar el menor de una lista

def small(lista):
    s = lista[-1]
    for element in lista:
        if element < s:
            s = element
    return s

#Retornar mayor de una lista

def big(lista):
    m = lista[-1]
    for element in lista:
        if element > m:
            m = element
    return m

#Retornar lista con numeros pares

def even(lista):
    new = []
    for element in lista:
        if element % 2 == 0:
            new.append(element)
    return new



def odd(lista):
    new = []
    for element in lista:
        if element % 2 != 0:
            new.append(element)
    return new

#Eliminar primera ocurrencia de x en una lista

def delete_ocurrency(lista, n):
    c = 0
    for element in lista:
        if element == n and c == 0:
            lista.pop(element)
            c += 1
    return lista

def delete_ocurrency_total(lista, n):
    new = []
    for element in lista:
        if element != n:
            new.append(element)
        elif element == n and element not in new:
            new.append(element)
    return new

# Insertar un elemento en una lista que esta ordenada y que quede ordenada

def insrt(lista, n):
    c = 0
    for i, element in enumerate(lista):
        if element == n and c == 0:
            lista.insert(i, n)
            c += 1
    return lista

# True si una lista esta ordenada, sino False

# def sorted(lista):
#     i = 0
#     while i < len(lista) -1:
#         if lista[i] > lista[i+1]:
#             return False
#         i += 1
#     return True

def sorted(lista):
    if lista == lista.sort():
        return True
    return False

print(sorted([4,2,3,4,5,6]))
