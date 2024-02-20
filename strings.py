
# учимся писать строки!

s = "hello, 'world'!"
print(s)

s = 'hello, "world"!'
s = """'hello,' "world"!"""
s = '''hello """,""" world!'''
s = 'hello \"world\"!' # экранирование

s = 'hello \nworld!' # перенос cтроки через \n


s = """hello, 
world!""" # перенос строки через тройные кавычки (ТРОЙНЫЕ КАВЫЧКИ ЕЩЕ ВЫДЕЛЯЮТ ДОКУМЕНТАЦИЮ)

"""
    Prints the values to a stream, or to sys.stdout by default.

      sep
        string inserted between values, default a space.
      end
        string appended after the last value, default a newline.
      file
        a file-like object (stream); defaults to the current sys.stdout.
      flush
        whether to forcibly flush the stream.
    """



# сырые строки

s = r"\n\n\n\"     # префикс r" - позволяет нам делать даже из спецсиволов и тд обычную строку


# индексы и слайды

s = "abcdefg"
print(s[1])  # из строки покажет второй символ т.е. 'b'
print(s[5])  # из строки покажет 6 символ т.е. 'f'
print(s[-1]) # из строки покажет второй символ но с конца т.е. 'e'

print(s[1:5]) # вырежет в диапазоне с 1 включительно и по 5 не включительно (с минусом инвертируется направление пересчета
print(s[1:5:2]) # доп цифра - это шаг т.е. через одну букву будет выводить

print(s[::-1]) # с шагом 1 начиная с конца выведет символы, т.е. по сути перевернет задом наперед строку всю если пуст знач ::
print(len[s]) # посчитает кол-во символов в строке (len - это длина)


# Оперируем

"Hello, world".title() # загл буквы кажд слова
"Hello, world".upper() # все буквы заглавные
"Hello, world".lower() # все буквы мелкие

i = "Hello, world".index('l') # показывает на каком месте порядково стоит символ
print(i)

s = 'https://google.com'.startswith('https://') # проверяет что строка начинается с конкретных значений (выведет True)
print(s)


# Форматируем

hello = 'Hello'
world = 'world'
s = hello + ', ' + world # КОНКАТЕНАЦИЯ!!! строк - склеивает строки  (s = "Hello, " + "world"), (s = hello + world)
print(s)

s = f'{Hello}, {world.upper()}!' # F строки - наиболее предпочт способ форматр строк
print(s)                         # (обычная строка но все что в фигурн скобках это типа код и будет исполняться, т.е. внутри выражения можем добавлять действия)

s = "{w}! {h}, {w}{w}{w}".format(h = hello, w = world) # До F строк было популярно так
print(s)


url_template = 'https://google.com/{}' # отложенное форматирование строки
url_template.format("my address")
url_template.format('another_address')


# Строку в число и наоборот


a = 123
s = "123" # символы одинаковые - тип данных разный (число всегда в строку можем, а строку в число только если там цифры, по понятным причинам)

assert int(s) == 123 # преобразует строку в число (и будут они равны)
assert s == str(a) # преобразует число в строку

