'''
Вашей программе на вход подается последовательность строк.
Первая строка содержит число n (1 ≤ n ≤ 100).
В следующих n строках содержится по одному целому числу.
Выведите одно число – сумму данных n чисел
'''
x = 0 #текущее слагаемое
lst =[]

digit_num = int(input('введите общее кол-во цифр: '))
for i in range (digit_num ):
    x= int(input('введите число {0}:'.format(i+1)))
    lst.append(x)
print(sum(lst))

x = 0 #текущее слагаемое
lst =[]
digit_num = int(input())
for i in range (digit_num ):
    x= int(input())
    lst.append(x)
print(sum(lst))