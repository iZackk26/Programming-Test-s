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
    copia = lista.copy()
    copia.sort()
    if lista == copia:
        return True
    return False

# La lista unicamente debe tener 1's y 0's, pero intercalados. De no ser asi se retorna False

def inter(lista):
    i = 0
    while i < len(lista) - 1:
        if lista[i] == 0:
            if lista[i + 1] != 1:
                return False
        elif lista[i] == 1:
            if lista[i + 1] != 0:
                return False
        i += 1
    return True

# Duplicar x elemento en una lista

def duplicate(lista, n):
    i = 0
    while i < len(lista) - 1:
        if lista[i] == n:
            lista.insert(i, n)
            i += 1
        i += 1
    return lista


#lista = [4, 100, 45, 50, 60, 200, 234, 550, 3]

# Ordenar una lista y hacer dos sublistas en las cuales se dividan en pares y pares
def sorty(lista):
    rows = len(lista) - 1
    while rows > 0:
        r1 = 0
        while r1 < rows:
            if lista[r1] > lista[r1+1]:
                lista[r1], lista[r1+1] = lista[r1+1], lista[r1]
            r1 += 1
        rows -= 1
    return lista


def odd_even(lista):
    odd = []
    even = []
    for element in lista:
        if element % 2 == 0:
            odd.append(element)
        else:
            even.append(element)
    # odd.sort() #Aca se puede utilizar el .sort() para acomodarla pero otra manera es haciendo cualquier metodo de ordenamiento como el quicksort, burbuja o insercion
    # even.sort()
    return even, odd


# lista = [4, 100, 45, 50, 60, 200, 234, 550, 3]


#Crear lista con divisores de un numero x, incluidos el 1 y el mismo

def divisors(n):
    data = []
    c = 1
    while c <= n:
        if n % c == 0:
            data.append(c)
        c += 1
    return data

#Crear una lista con los numeros primos que esten antes de x

def prime_list(number):
  data = []
  for n in range(2, number + 1):
    prime = True
    for i in range(2, n):
      if n % i == 0:
        prime = False
        break
    if prime:
      data.append(n)
  return data

# Recibe una lista con sublistas en los cuales hay que pasar todo a una lista y luego ordenarlos

def ext(lista):
    data = []
    for sublist in lista:
        data.extend(sublist)
        data.sort()
    return data
lista = [[89, 2, 4],[45, 1],[33, 22], [9]]


# Ejercicio imprimir indice de cada elemento en las sublistas
lista = [[1, 11, 10], [33, 456, 1, 32], [34, 66, 78, 98, 99, 1, 29]]

def groups_indx(lista):
    i = 0
    data = []
    for sublist in lista:
        base = 0
        while base < len(sublist):
            if base == 0:
                data.append([sublist[base],2])
            if base == 1:
                data.append([sublist[base],8])
            if base == 2:
                data.append([sublist[base], 10])
            base += 1
        i += 1
    return data

print(groups_indx(lista))

                




print(groups_indx(lista))
