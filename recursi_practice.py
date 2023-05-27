# Sum every number until a flag number recursibly

def sum_until(n):
    if n == 0:
        return 0
    return n + sum_until(n-1)

# Calculate a Factorial Function recursibly

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Calculate fibbonacci fuction recursibly

def fibbonacci(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    else:
        return fibbonacci(x-1) + fibbonacci(x-2)


# Calculate the elevated number recursibly, we need the base and the exponent

def elevated(base, exp):
    if exp == 0:
        return 1
    else:
        return base * elevated(base, exp-1)


# Calc the sum of all the elements in a list

def sum_list(lista):
    if not lista:
        return 0
    else:
        return lista[0] + sum_list(lista[1:])

# Calc the elements in a list and show how many there are

def count_elements(lista):
    if not lista:
        return 0
    else:
        return 1 + count_elements(lista[1:])

# print(count_elements([1,2,3]))

# Invert an str recursibly

def inver_str(text):
    if len(text) == 0:
        return text
    return inver_str(text[1:]) + text[0]


# Search an specific element in a list and return the idxo

def search_idx(lista, element, idx = 0):
    if not lista:
        return -1
    elif lista[0] == element:
        return idx
    else:
        return search_idx(lista[1:], element, idx + 1)

# print(search_idx([1,3,2,4], 2))
            

