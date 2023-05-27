marcianos = [ ["Mar1",  [ ["Traje", 800, 2],   ["Sombrero", 50, 2],   ["Paraguas", 100, 1] ] ],["Mar2",  [ ["Abrigo", 1000, 1], ["Palomitas", 1500, 1] ] ]]

for marciano in marcianos:
    result = 0
    for item in marciano[1]:
        result += item[1] * item[2]
    print("El marciano gasto un total de:", result)


