def div(a,b):
    return a/b if b != 0 else ZeroDivisionError


print(div(int(input('Введите числитель: ')),int(input('Введите знаменатель: '))))
