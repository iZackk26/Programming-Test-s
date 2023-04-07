#Escribir una función que retorne el menor número de una lista. Ejemplo: [3,4,2,77,45,44] ->2
def big(list):
    big = 0
    for x in list:
        if x > big:
            big = x
    return big

def small(list):
    big_number = big(list)
    for x in list:
        if x < big_number:
            big_number = x
    return big_number

#Escribir una función que retorne el mayor número de una lista. Ejemplo: [3, 4,2, 77, 45, 44] ->77

def big(list):
    big = 0
    for x in list:
        if x > big:
            big = x
    return big

# Escribir una función recibe una lista de enteros y retornar una lista con
# números pares. Ejemplo: [2, 3, 6, 4, 6] -> [2, 6, 4, 6]

def list_pares(list):
    for x in list:
        if x % 2 != 0:
            list.remove(x)
    return list


# Escribir una función que Recibe una lista de enteros y retornar una lista con
# los números impares. Ejemplo: [2, 3, 6, 4, 6] -> [3]

def list_pares(list):
    for x in list:
        if x % 3 != 0:
            list.remove(x)
    return list

# Escribir una función que quita la primera ocurrencia de x en L. Se debe retornar
# una lista que no contenga la primera ocurrencia de x. Ejemplo: Eliminar la
# primera ocurrencia de 4 en [4, 2, 3, 4, 5, 4, 7] -> [2, 3, 4, 5, 4, 7]

def delete_first_repeated(n,list):
    y = 0
    for x in list:
        if x == n and y == 0:
            list.remove(x)
            y += 1
    return list


# Escribir una función que quita todas ocurrencia de x en L. Se debe retornar una
# lista que no contenga x. Ejemplo: Eliminar todas las ocurrencias de 4 en [4, 2,
# 3, 4, 5, 4, 7] -> [2, 3, 4, 5, 7]

def delete_repeated(n,list):
    count = 0
    for x in list:
        if x == n :
            count += 1
            if count > 1:
                list.remove(x)
    return list

# Escribir una función que inserta un elemento x en una lista ordenada tal que
# retorne una lista ordenada. Ejemplo: insertar 4 en [1, 2, 3, 3, 4, 5, 5, 6, 7]
# -> [1, 2, 3, 3, 4, 4, 5, 5, 6, 7]

def add_and_sort(n,list):
    count = 0
    quantity = 0
    for x in list:
        if x == n and quantity == 0:
            list.insert(count,n)
            quantity += 1
        count += 1
    if n not in list:
            list.append(n)
    return list

# Escribir una función que retorne True si una lista de números está ordenada
# ascendentemente. Ejemplo: [1, 2, 3, 3, 4, 5, 6, 6, 7, 77] ->True

def sort_list(list):
    for i in range(len(list)-1):
        if list[i] > list[i + 1]:
            return False
    return True

def alternate_list(list):
    i = 0
    for x in list:
        if x == 0:
            if i < len(list)-1 and list[i] == list[i + 1]:
                return False
        if x == 1:
            if i < len(list) -1 and list[i] == list[i + 1]:
                return False
        i += 1
    return True

#Siguiente Ejercicio

def duplicate(n,list):
    new_list = []
    for x in list:
        new_list.append(x)
        if x == n:
            new_list.append(n)
    return new_list

list_3 = [1,2,3,4,2]

#Ejercicio 2 listas

def odd_and_even(list):
    odd = []
    even = []
    for number in list:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    return odd, even

def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

def sort(odd, even):
    odd_list = bubble_sort(odd)
    even_list = bubble_sort(even)
    return odd_list, even_list

lista = [3,1,6,8,2,8,4,5,7]
odd, even = odd_and_even(lista)
print(sort(odd,even))
