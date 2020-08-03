'''
Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.
Или эквивалентно записи:
class Class1(Class2, Class3 ... ClassK):
    pass



'''

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return None
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_path(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

dict={}
n = int(input())
'''
for i in range(n):
    a, *b = input().replace(":", " ").split()
    if a not in dict:
        dict[a]=b
    else:
        for key,val in dict.items():
            if key == val:
                dict[key]=val + b
print(dict)
'''
'''
m = int(input())
for i in range(m):
    fin, st = input().split()

    if fin == st and fin in dict:
        print('Yes')
    elif fin == st and fin not in dict:
        print('No')
    else:
        if find_path(dict, fin, st) == []:
            print('Yes')
        else:
            print('No')

'''



'''
3
Q : P
Q : R
Q : S
2
1 1
Q 
Если ключа а нет словаре, то dict[a] = b, иначе проверяю в цикле по ключам key и значениям value,
 если ключ совпадает со значением, то  dict[key] = value + b
 3. Создаю функцию для формирования пути от потомка к родителю. Использовала функцию из http://www.infocity.kiev.ua/prog/python/content/pytonesse_3.shtml
Я ее переопределила (мне так было проще)
def find_path(graph, end, start, path=[]):
и немного видоизменила
for node in graph[start]:
    if node not in path:
Соответственно в теле поменяются начало и конец. Например, newpath = find_path(graph, end, node, path)
4. В цикле ввожу fin, st = input().split(). Вызываю find_path(dict, fin, st). И если функция возвращает путь, то печатаю "Yes", иначе - печатаю "True"
'''