def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
print(dfs(graph, 'A'))

graph1 = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
from queue import deque


def bfs1(graph, start):
    visited, queue = [], deque([start])
    while queue:
        vertex = queue.pop()
        if vertex not in visited:
            visited.append(vertex)
            queue.extendleft(set(graph[vertex]) - set(visited))
    return visited

print(bfs1(graph1, 'A'))

'''
Использовал работа с графами - поиск в ширину - https://pimiento.github.io/python_graphs.html

Искал родителей исключения из запроса на их обработку.

По мере просмотра исключений из запроса формировал список ранее просмотренных исключений.

Просматривал имеются ли родители исключения в ранее уже просмотренных исключениях.

Если да - выводил их в ответ, но только после проверки, что они ранее уже не выводились (для исключения повторений в выводе).
'''