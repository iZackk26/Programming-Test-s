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

#Ejercicio 6

def delete_first_repeated(n,list):
    y = 0
    for x in list:
        if x == n and y == 0:
            list.remove(x)
            y += 1
    return list


# Ejercicio 7
def delete_repeated(n,list):
    count = 0
    for x in list:
        if x == n :
            count += 1
            if count > 1:
                list.remove(x)
    return list

#Ejercicio 8

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

#Ejercicio 9
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

#Siguiente 10

def duplicate(n,list):
    new_list = []
    for x in list:
        new_list.append(x)
        if x == n:
            new_list.append(n)
    return new_list

list_3 = [1,2,3,4,2]

#Ejercicio 11 listas

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

# lista = [3,1,6,8,2,8,4,5,7]
# odd, even = odd_and_even(lista)
# print(sort(odd,even))

# Ejercicio #12

def divisors(n):
    new_list = []
    div = 1
    while div <= n:
        if n % div == 0:
            new_list.append(div)
        div += 1
    return new_list
# print(divisors(8))

#Ejercicio #13

def prime(n):
    div = 2
    while div < n:
        if n % div == 0:
            return False
        div += 1
    return True
# print(prime(8))

def adding_prime(n):
    count = 2
    prime_list = []
    while count < n:
        if prime(count) == True:
            prime_list.append(count)
        count += 1
    return prime_list

#Ejercicio #14

def bubble_sublist(list):
    n = len(list)
    i = 0
    for sublist in list:
        for subsublist in sublist:
            for j in range(n-i-1):
                if list[j] > list[j+1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
