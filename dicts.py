
# заводим словарики
# набор двух списков которые которые друг с другом как то соотносятся (это набор пар получается) пара "ключ-значение" по этому ключу всегда можем получить значение
# удобный способ например в списке найти конкретное значение за постоянное время

d = {"key": "value"}
d = {
    "name": "Олег",
     "age": 28
     }

name = d["name"]
print(name)

d["age"] += 1 # прибавить 1 год Олегу (сокращаем запись d["age"] = d["age"] +1)

# функции словарей

d.items() # и то и то в паре
d.keys() # все ключи
d.values() # все значения

print(d.get("unexpected")) # Позволяет избежать ошибки отсутствия ключа, проверить (если нет - то получим None)
print(d.get("unexpected", "default value")) # получим "default value" если нет ключа который ищем, т.е. сначала сверяет наличие ключа и если отриц ответ то получим default value которое укажем следом
print(d.get("age", "default value")) # получим значение - 29, в данном случае, т.к. ключ есть такой
# d[unexpected] # так ничего не получим - только ошибку! 

