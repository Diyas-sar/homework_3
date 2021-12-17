def int_func(a):
    for el in range(len(a)):
        a = a.title()
    return a


print(int_func('text text'))