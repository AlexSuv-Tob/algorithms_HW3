"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
subs_n = set()

def subs_set(subs):
    subs = str(subs)

    for i in range(len(subs)):
        for j in range(len(subs) - 1 if i == 0 else len(subs), i, -1):
            subs_n.add(hash(subs[i:j]))
    return subs

print(subs_set(input("Введите строку: ")))
print(f'количество подстрок в строке = {len(subs_n)}')


