# Function that counts the digits of a number

def count_digits(n: int)-> int:
    if n == 0:
        return 0
    return 1 + count_digits(n//10)

# print(count_digits(7654))

# Function that tells how many times does x number is repeated
def repeated_digit(n: int, repeat: int)-> int:
    if n == 0:
        return 0
    elif n % 10 == repeat:
        return 1 + repeated_digit(n//10, repeat)
    return repeated_digit(n//10, repeat)

# print(repeated_digit(12131,1))

# Function that tells how many times each number repeats

def each_repeated(number, dic):
    if number == 0:
        return dic
    
    last_digit = number % 10
    if last_digit in dic:
        dic[last_digit] += 1
    else:
        dic[last_digit] = 1
    
    return each_repeated(number // 10, dic)

# x = each_repeated(123123123, {})
# for digit, count in x.items():
#     print(f"El dígito {digit} se repite {count} veces.")


# invert a number

def invert_number(n, result):
    if n == 0:
        return result
    digit = n % 10
    result = result * 10 + digit
    return invert_number(n//10, result)

# print(invert_number(123,0))


for quantity in range(10):
    x= int(input("Numbah plz"))
    print(invert_number(x,0))


