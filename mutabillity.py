# # Списки, словари и множества - изменяемые!
# # mutabillity - это изменяемость данных, в контексте питона это означает что у нас есть разные типы данных
# # Со строкой например не прокатит - она не изменяемая , она копируется и возвращается новая с изм. а списки словари и множества изменяемые


from copy import deepcopy

a = [1,2,3]
b = a

b.append(4) # изменятся оба списка т.к. они буквально ссылаются на одно и тоже значение

print(a)
print(b)

a = [1,2,3]
b = a.copy()

b.append(4) # изменятся оба списка

print(a)
print(b)


a = [1, 2, 3, [4, 5, 6]] # список в списке
b = a.copy()
b[-1].append(7) # скопировали и добавили 7 но получим копию верхнеуровнего списка, а вложенный так и будет ссылаться на одно и то же и 7 добавится везде (т.е. функция copy копирует только первый слой этого списка (но не вложенный)

print(a)
print(b)


a = [1, 2, 3, [4, 5, 6]] # список в списке
b = deepcopy(a)
b[-1].append(7) # использую библиотеку deepcopy (меняем copy на deepcopy) и тогда уже скопируются все слои и поэтому будет изменятся только второй

print(a)
print(b)


# exit(0) # это для того чтобы код ниже этой строки не исполнялся


# Кортежи, frozenset - нет

a = (1, 2, 3, "4", "5")
a[0] = 123 # кортежи не поддерживают присвоение значений

a. #в методах собственно кроме index и count ничего и нет (потому что остальные методы как у списка так или иначе меняют значения


a = (1, 2, 3, "4", "5")
b = a  # благодаря тому что он постоянный тут не допустишь ошибок с копированием, кортеж правдиво скопируется в таком варианте. за счет этого он быстрее.

d = {"key": "value", "first": "second"}
dd = (("key": "value"), ("first": "second")) # чтобы сделать словарь не изменяемым то можно хранить словарь в кортеже с кортежами



frozenset([1, 2, 3, 4, 5]).  # тот же сет но не изменяемый!