
# boolean - 3 состояния

b = bool # true/false
t = True
f = False
n = None # Не относится к boolean но оч близко

# If/Elif/Else - на примере кода отчета

if True:
    print("правда!")
else:
    print("ложь!") # выводится только что-то одно, смотря какое условие выполняется.

code = 200

if 200 <= code < 300: # if code >= 200 and < 300: / упростить при вхождении в диапазон переменной if 200 <= code < 300:
    print("все хорошо!")
elif 400 <= code < 600: # elif позволяет добавить еще одно условие для проверки.
    print("все плохо!")
else:
    print("все неопределенно") # сюда будет попадать диапазон 300ых который и не плохо и не ожидали например.

# Пустые объекты - false

print(bool(10))  # True
print(bool(-10))  # True
print(bool(0))  # False
print(bool("abcdefg"))  # True
print(bool(""))  # False
print(bool("0"))  # True
print(bool([]))  # False
print(bool([1,2,3]))  # True
print(bool({}))  # False
print(bool({"key": 123}))  # True
print(bool(None))  # False

users = []

if users:
    print(users)
