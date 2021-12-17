def my_func(x, y):
    a=1
    for el in range(abs(y*-1)):
        a = a*x
    return 1/a

print(my_func(2,-2))