'''
В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.
Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.
Примечание:
Для решения этой задачи используйте стандартный модуль datetime.
Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате.
 Sample Input 1:
2016 4 20
14
Sample Output 1:
2016 5 4
'''
import datetime

year, month, day = map(int, input().split())
#print(year, month, day)
beg_date = datetime.datetime(year, month, day)
#print(beg_date)
date_to_add=datetime.timedelta(days=int(input()))
end_date = beg_date + date_to_add
print(end_date.year, end_date.month, end_date.day)

d = datetime.date(*[int(i) for i in input().split()]) + datetime.timedelta(days = int(input()))
#создаем список от входных данных
i=[int(i) for i in input().split()]
# разименовываем списк при передаче в функцию date
print(datetime.date(*i))