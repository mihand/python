
'''
{'BaseException': [], 'Exception': ['BaseException'], 'LookupError': ['Exception'], 'KeyError': ['LookupError']}
http://www.infocity.kiev.ua/prog/python/content/pytonesse_3.shtml
4
BaseException
Exception : BaseException
LookupError : Exception
KeyError : LookupError
2
BaseException
KeyError

Output:
KeyError
'''


#import queue
from queue import deque
#работа с графами
#https://pimiento.github.io/python_graphs.html
# Bread-Firsth Search — Поиск вширину
# Позволяет найти кратчайший путь между двумя вершинами.
# Довольно сложно реализовать рекурсивно, гораздо проще реализовать его с использованием очереди.
def bfs(graph, start):
    visited, queue = [], deque([start])
    while queue:
        vertex = queue.pop()
        if vertex not in visited:
            visited.append(vertex)
            queue.extendleft(set(graph[vertex]) - set(visited))
    return visited

dict={}
n = int(input())

for i in range(n):
    a, *b = input().replace(":", " ").split()
    if a not in dict:
        dict[a]=b
    else:
       dict[a]=dict[a] + b
       #print(dict)

m = int(input())
exception_list=[]

for _ in range(m):
    #запрос на обработку исключения
    exception = input()
    if exception in exception_list:
        print(exception)
    else:
        # Поиск родителей запрошенного исключения
        par =(bfs(dict, exception))
        flg = False
        for i in par: # возвращается лист из одного или нескольких значений
            if i in exception_list:
                # имеются ли родители исключения в ранее уже просмотренных исключениях?
                flg = True
                break
        if flg == True:
            print(exception) # выводим их в ответ
        else:
            # формируем список ранее просмотренных исключений.
            exception_list.append(exception)



