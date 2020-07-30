'''
Пусть n = 3, т. е. есть три элемента (1, 2, 3). Пусть k = 2.
Все различные сочетания из 3 элементов по 2: (1, 2), (1, 3), (2, 3).
Различных сочетаний три, поэтому C(3, 2) = 3.
Для вычисления C(n, k) в других случаях используется следующая рекуррентная формула:
C(n, k) = C(n - 1, k) + C(n - 1, k - 1).
Реализуйте программу, которая для заданных n и k вычисляет C(n, k).
Вашей программе на вход подается строка, содержащая два целых числа n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).
Ваша программа должна вывести единственное число: C(n, k).
'''

def calc(n, k):
    # если C(n, 0) = 1, так как из n элементов выбрать 0 можно единственным образом, а именно, ничего не выбрать.
    if k == 0 :
        return 1
    #если     k > n, то    C(n, k) = 0, так     как    невозможно, например, из    трех    элементов    выбрать    пять.
    elif k > n:
        return 0
    else:
        return calc(n - 1, k) + calc(n - 1, k - 1)

n, k = map(int, input().split())
print(calc(n,k))


