def sum_number(n):
    if n == 0:
        return 0
    return n + sum_number(n-1)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def fibbonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)

def elevated_number(n, idx):
    if idx == 0:
        return 1
    return n * elevated_number(n, idx -1)

def sum_list(lista):
    if not lista:
        return 0
    else:
        return lista[0] + sum_list(lista[1:])

def binary(digit, idx = ""):
    if digit == 0:
        print(idx)
    else:
        binary(digit-1, idx + "0")
        binary(digit -1, idx + "1")

# binary(3)


def count_list_elemets(lista):
    if not lista:
        return 0
    else:
        return 1 + count_list_elemets(lista[1:])


def invert_str(text):
    if not text:
        return ""
    else:
        return invert_str(text[1:]) + text[0]


def search_element(lista, element, idx = 0):
    if not lista:
        return False
    if lista[0] == element:
        return idx
    else:
        return search_element(lista[1:], element, idx + 1)


# print(search_element([1,2,3,4,1,2,3], 4))


def hanoi(n, origin,destinatio, aux):
    if n == 1:
        print(f"El disco en la torre {origin}, se mueve hacia la torre{destinatio}")
        return
    else:
        hanoi(n-1, origin, aux, destinatio)
        print(f"El disco en la torre {origin}, se mueve hacia la torre{destinatio}")
        hanoi(n-1, aux, destinatio, origin)


def check_binary(n):
    if n == 0:
        return True
    elif n % 10 > 1:
        return False
    else:
        return check_binary(n//10)

# print(check_binary(2010))


def descript(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return (n % 5 + descript(n//10) * 10)
    else:
        return (n % 10 +descript(n//10) * 10)

print(descript(83654))
