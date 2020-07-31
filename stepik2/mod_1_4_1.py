# = {'global': {'parent': None, 'variables': set()}}
scopes = {'global': {'parent': None, 'vars': []}}

def create(namespace, parent): # создать новое пространство имен с именем <namespace> внутри пространства <parent>
    #scopes = {'global': {'parent': 'None', 'vars': []}}
    if namespace not in scopes: #если такого namespace нет в словаре scopes
        if parent in scopes:    # и если есть такой родитель
            scopes[namespace] = {} #создаем новый словать в словаре scopes
            scopes[namespace]['parent'] = parent
            scopes[namespace]['vars'] = []
            return scopes
    else:
        return None

def add (namespace, var):  #добавить в пространство <namespace> переменную <var>
    #scopes = {'global': {'variables': ['a'], 'parent': None }}
    if namespace in scopes:
        if var not in scopes[namespace]['vars']:
           scopes[namespace]['vars'].append(var)
           return scopes
    else:
        return None

# получить имя пространства, из которого будет взята переменная <var> при запросе из пространства <namespace>,
#или None, если такого пространства не существует
'''<namespace>, если в пространстве <namespace> была объявлена переменная <var>
get <parent> <var> – результат запроса к пространству, внутри которого было создано пространство <namespace>, если переменная не была объявлена
None, если не существует <parent>, т. е. <namespace>﻿ – это global
'''
def get (namespace, var):
    if  var in scopes[namespace]['vars']:
        return namespace
    elif scopes[namespace]['parent'] is None:
        return None
    else:
        return get (scopes[namespace]['parent'], var)


#n = int(input('кол-во команд?: '))
n = int(input())
for i in range(n):
    #cmd, namesp, arg = input('введите команду namespace arg: ').split()
    cmd, namesp, arg = input().split()
    if cmd == 'create':
        create(namesp, arg)
    elif cmd ==  'add':
        add(namesp, arg)
    else:
        print(get(namesp, arg))