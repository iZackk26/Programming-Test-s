def sum_off(n:int)-> int:
    if n == 0:
        return 0
    return n + sum_off(n-1)

def factorial(n:int)->int:
    if n == 0:
        return 1
    return n * factorial(n-1)

def fibbonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)

def elevated(n:int, exponent:int )-> int:
    if exponent == 0:
        return 1
    return n * elevated(n, exponent -1)

def sum_of_list(lista:list)-> int:
    if not lista:
        return 0
    return lista[0] + sum_of_list(lista[1:])

def binary(n, complement = ""):
    if n == 0:
        print(complement)
    else:
        binary(n-1, complement + "0")
        binary(n-1, complement + "1")

def count_elements(lista:list)-> int:
    if not lista:
        return 0
    return 1 + count_elements(lista[1:])


def invert_str(text:str)-> str:
    if not text:
        return ""
    return invert_str(text[1:]) + text[0]

def search_idx(lista: list, idx: int = 0, searcher = 0)-> int:
    if not lista:
        return False
    if lista[0] == idx:
        return idx
    return search_idx(lista[1:], idx, searcher +1)

def hanoi(n, origin, destination, aux):
    if n == 1:
        print(f"Mover disco de la torre {origin} a la torre {destination}")
    else:
        hanoi(n-1 ,origin, aux, destination)
        print(f"Mover disco de la torre {origin} a la torre {destination}")
        hanoi(n-1, aux, destination, origin)
# hanoi(3,"A","B","C")

def is_binary(n):
    if n == 0 or n == 1:
        return True
    elif n % 10 == 1 or n % 10 == 0:
        return is_binary(n//10)
    else:
        return False

def desencript(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return (n % 5 + desencript(n//10) * 10)
    else:
        return (n % 10 + desencript(n//10) * 10)

# print(desencript(83654))


def binary(n):
    if n == 0:
        return True
    elif n % 10 > 1:
        return False
    else:
        return binary(n//10)


def octal(n):
    if n == 0:
        return True
    elif n % 10 == 8:
        return False
    else:
        return octal(n//10)


# There are several ways to do this algorithm

def binary_to_decimal(n, result=0):
    if n == 0:
        return result
    else:
        result = (result + n % 10) * 2
        return binary_to_decimal(n // 10, result)


def binary_to_deci(n, result = 0):
    if n == 0:
        return result
    else:
        result = result + (n % 10) * (2 ** len(str(n)))
        return binary_to_deci(n//10, result)


def octal_to_decimal(n, result = 0):
    if n == 0:
        return result
    else:
        result = result + (n % 10) * (8**len(str(n)))
        return octal_to_decimal(n//10, result)

# print(octal_to_decimal(10))
 

def deci_octal(n, result=0, count=0):
    if n == 0:
        return result
    else:
        result = result + (n % 8) * (10 ** count)
        return deci_octal(n // 8, result, count + 1)

# print(deci_octal(10))


def deci_binary(n, result = 0, count = 0):
    if n == 0:
        return result
    else:
        result = result + (n % 2) *(10**count)
        return deci_binary(n//2, result, count+1)


# print(deci_binary(10))


