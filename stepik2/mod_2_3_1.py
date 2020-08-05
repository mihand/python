'''
self.iterable=iterable здесь у нас переменные [1,2,3,4]
self.funcs=funcs   здесь внешние функции [f1(),f2(),f3()] , в которые мы отправляем переменную и нам возвращается тру\фолс
self.judge=judge  а тут собственно одна из наших функций, которые мы реализовали выше.

def __iter__(self):
   тут мы реализуем проверку наших переменных, берем переменную, скармливаем её поочередно внешним функциям,
    приплюсовываем тру или фолс, по итогу зовем свою функцию и спрашиваем её стоит ли нам елдить
     переменную или берем следующую. беря следующую не забудьте сбросить счетчик pos(тру)\neg(фолс)
'''

class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg
    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos >= 1
    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0
    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        self.iterable = iterable
        # funcs - допускающие функции
        self.funcs = funcs
        # judge - решающая функция
        self.judge = judge
    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        for i in self.iterable:
            results = [f(i) for f in self.funcs]
            if self.judge(results.count(True), results.count(False)):
                yield i

def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]