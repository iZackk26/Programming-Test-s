# fuction that sums n quantity of numbers

def sum(n):
    if n ==0:
        return 0
    return n + sum(n - 1)

# print(sum(8))

#Factorial fuction

def factorial(n):
    if n ==0:
        return 1
    return n * factorial(n-1)

# print(factorial(5))

# Fibbonacci secuence

def fibbonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)

# print(fibbonacci(4))

# Function that return A value elevated to B

def elevation(base, exp):
    if exp == 0:
        return 1
    else:
        return base * elevation(base, exp-1)

# print(elevation(2,3))
# See this in the debugger to be more clear

# Sumatoria de una lista de elementos

def sum_list(lista): # [1,2,3,4,5]
    if lista == []:
        return 0
    else:
        return lista[0] + sum_list(lista[1:])

# print(sum_list([1,2,3,4,5,6,7,8]))

# Imprimir todos los numertos binarios de n digitos

def imprimir_binarios(n, prefijo=""):
    if n == 0:
        print(prefijo)
    else:
        imprimir_binarios(n - 1, prefijo + "0")
        imprimir_binarios(n - 1, prefijo + "1")

# imprimir_binarios(3)




# funcion que retorna la cantidad de elementos de una lista

def count_list(lista):
    if lista == []:
        return 0
    return 1 + count_list(lista[1:])

# print(count_list([1,2,3,4]))


# funcion que retorne una cadena de texto invertida

def inver_str(text):
    if len(text) == 0:
        return text
    return inver_str(text[1:]) + text[0]

print(inver_str("Hola"))


# Funcion la cual busque un elemento en una lista de manera recursiva y encuentre el indice de dicho elemento


def buscar_elemento(lista, elemento, indice=0):
    if not lista:
        return -1  
    elif lista[0] == elemento:
        return indice  
    else:
        return buscar_elemento(lista[1:], elemento, indice + 1)

# print(buscar_elemento([1,2,3,4,5,6], 6))


