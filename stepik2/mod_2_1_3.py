'''
Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел.
Также реализуйте новое исключение NonPositiveError.
В классе PositiveList переопределите метод append(self, x) таким образом, чтобы при попытке добавить неположительное целое число бросалось исключение NonPositiveError и число не добавлялось, а при попытке добавить положительное целое число, число добавлялось бы как в стандартный list.
В данной задаче гарантируется, что в качестве аргумента x метода append всегда будет передаваться целое число.
Примечание:
Положительными считаются числа, строго большие нуля.
'''
class Error(Exception):
    """Base class for other exceptions"""
    pass
class NonPositiveError(Error):
    """Raised when the input value is too small"""
    pass

class PositiveList(list):
    def append(self, x):
        if x > 0:
           # y= super(PositiveList, self).append(x)
            super().append(x)
        else:
            raise NonPositiveError


x= PositiveList()
x.append(-2)
print(x)