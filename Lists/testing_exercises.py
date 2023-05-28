#[22, 101, 120, 45, 66, 69, 83, 76, 99, 33] --> [22, 101, 120, 45, 66, 76, 33]

def is_octal(lista):
    for i, element in enumerate(lista):
        while element > 0:
            if element % 10 == 8:
                lista.pop(i)
            element //= 10
    return lista

lista = [22, 101, 120, 45, 66, 69, 83, 76, 99, 33]

# print(is_octal(lista))

# Ejemplo: [[10, 2], [10, 99], [2, 101], [10, 49], [2, 111], [10, 94], [8, 45], [2, 11], [8, 77]].

def base(lista):
    octa = []
    binary = []
    deci = []
    for sublist in lista:
        if sublist[0] == 10:
            deci.append(sublist[1])
        if sublist[0] == 2:
            binary.append(sublist[1])
        if sublist[0] == 8:
            octa.append(sublist[1])
    # print("Los numeros en octal son:", octa, "Los numeros en binario son:", binary, "Los numeros en decimal son:", deci)
    return [deci, octa, binary]

x= [[10, 2], [10, 99], [2, 101], [10, 49], [2, 111], [10, 94], [8, 45], [2, 11], [8, 77]]
# base(x)


def insertion_sort(lista):
    data = []
    bina = lista[2]
    while len(bina) > 0:
        big = max(bina)
        data.append(big)
        bina.remove(big)
    return data

# print(insertion_sort(base(x)))

lista = [1,2,3,4,56,90,12]
# print(max(lista))


def bubble_sort(lista):
    octa = lista[1]
    pasadas = len(octa)-1
    while pasadas > 0:
        vueltas = 0
        while vueltas < pasadas:
            if octa[vueltas] > octa[vueltas+1]:
                octa[vueltas], octa[vueltas+1] = octa[vueltas+1], octa[vueltas]
            vueltas += 1
        pasadas -= 1
    return octa

# print(bubble_sort(base(x)))

# print(base(x))


def quicks_sort(lista):
    if len(lista) >=1:
        pass



lista = [[1,2,3],[3,4,5]]






