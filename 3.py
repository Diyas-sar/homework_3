def my_func(a,b,c):
    if a > b and b > c:
        return a + b
    if a > b and c > b:
        return a + c
    if c > a and b > a:
        return c + b
    else: print("Некоторые аргументы равны")
print(my_func(5,6,7))