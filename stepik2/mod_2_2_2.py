'''
Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.
Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать, какой из паролей служит ключом для расшифровки файла с интересной информацией.

Устанавливаем модуль pycryptodome (в pycharm открываем file->setting->project->  project interpreter->
 в окошке жмем знак '+' и в открывшемся окне ищем pycryptodome, жмем install package).
 Ставится без проблем. ﻿Далее качаем с официального сайта библиотеку https://pypi.python.org/pypi/simple-crypt.
  Далее распаковываем ﻿папку и заходим внутрь распакованного архива.
   Далее ищем там папку simplecrypt(прям ее одну, это важно , ﻿путь к ней:  simple-crypt-4.1.7/src/simplecrypt)
    ﻿ и копируем ее ﻿в корень нашего проекта, далее пробуем писать import simplecrypt
'''

import simplecrypt
import urllib
from urllib import request

encr_text = urllib.request.urlopen('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').read()
pwds = urllib.request.urlopen('https://stepic.org/media/attachments/lesson/24466/passwords.txt').read().strip().split()

print(encr_text)
print(pwds)

for pwd in pwds:
    try:
        str = simplecrypt.decrypt(pwd, encr_text)
        print(str.decode("utf-8"))
        break
    except simplecrypt.DecryptionException:
        print('неверный пароль')
