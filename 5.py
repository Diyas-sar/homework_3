b = 0
a = ''
while True:
    a = input("Ведите число: ")
    if a == "R":
        break
    for el in range(len(a)):
        if a[el] !=" " and a[el] !="R":
            b = b + int(a[el])
    print(b)
    if 'R' in a:
        break

