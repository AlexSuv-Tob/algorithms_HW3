"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib

salt = 'login'
a_list = []

def kash_url(url):
    res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()

    if res in a_list:
        print('Такой адрес уже есть')
    else:
        a_list.append(res)
        print('Добавили адрес в кэш')
    return a_list

print(kash_url(input('Введите адрес сайта: ')))
