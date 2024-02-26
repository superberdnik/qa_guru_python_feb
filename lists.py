# Делаем списки [list]  -- сортированный всегда

l = []
l = [1, 2, 3, 4, 5]
l = [1, 2, "3", "4", 5, [1, 2, 3]]

# l[0:1:-1] обращение к элементу по идексу
print(l[-1][1])

# Функции списков

l[0] = 10 # заменить первый элемент по индексу
print(l)

l.pop(0) # удалить первый по индексу элемент
print(l)

l.append(150)
print(l)

l.extend([[1, 2, 7]]) # добавляет список, если 2 раза поставить [] то добавится вложенный список
print(l)

l.reverse()
print(l)

print(list("abcdef")) # приведение строки в список

# "\n".join(l) # join на вход который список получает


# Множества (set)  --(порядка нет, не сортированный, только уникальные элементы в отличии от списка)

s = set([10, 9, 2, "5", 6, 5, 6]) # Один из способов оставить только уникальные элементы в списке - преобразовать список во множество, а потом опять в список
print(s)

ss = s | {1, 2}
ss = s & {1, 2}