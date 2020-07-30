'''
Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и возвращающую самое маленькое целое число y, такое что:
    y больше или равно x
    y делится нацело на 5
На вход функция принимает целое число. В теле функции - проверяем делится ли это число без остатка на 5.
Если нет увеличиваем его и проверяем снова. Как только нашлось такое число то выводим его из функции.
'''

def closest_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        y = x + 1
    return closest_mod_5(y)


inp = int(input('введите число: '))
print(closest_mod_5(inp) )