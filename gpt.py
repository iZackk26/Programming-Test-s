def euclides(a,b):
    if b == 0:
        return a
    return euclides(b, a%b)

print(euclides(10,2))

# Busqueda Binaria
def binary_search(arr, target, low, high):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)



# Calculo Binomial
def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

