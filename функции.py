import functools


# Объявляем функцию

def my_awesome_func():
    a = 5
    b = 10
    print(a + b)


my_awesome_func()


# Функция с позиционными аргументами


def sum_numbers(a, b):
    print(a + b)


# функция выполняется всегда одинаково, че не вставь логика одинаковая будет (без значения ошибка будет)


sum_numbers(10, 15)
sum_numbers(50, 100)
# sum_numbers(50, "100") -- такая функция упадет потому что передаешь чушь (плохие аргументы)

# Функция с именованными аргументами, она гораздо более наглядна

sum_numbers(a=10, b=15)  # преимущество в том что можем менять местами именованные функции
sum_numbers(b=50, a=15)

# Функция с аргументами по умолчанию

print(1, 2, 3, 4, 5, sep="\n")


def multyply(a, b=10):
    print(a * b)


multyply(5)
multyply(5, 7)

day = "monday"


def my_func():
    def another_func():
        print(func_day)  # здесь тоже сможет использоваться объявленная ниже переменная func_day

    day = "suturday"
    func_day = "saturday"  # в функции можем переобъявить переменную
    print(day, func_day)


# все что внутри функции объявлено то и работает в этой функции или при функции в функции работает на уровень выше


my_func()
print(day)  # вне функции будет все равно monday


# print(func_day) -- не сущ вне функции? нет такой переменной


# Возвращаем значение


def sum_numbers(a, b):
    return a + b


result = sum_numbers(10, 15)
print(result)

# Переменное количество аргументов на примере print


print(2, 3, 5, 10, 3546, "sfdh",
      "sdf")  # про *args, все что перечисляется кладет в *args, sep end и тд только по имени, иначе дефолтн значение


def sum_numbers(*args):
    result = 0
    for number in args:
        result += number
    print(result)

    print(sum(args))  # это делает тоже самое что и 86-89строки


sum_numbers(10, 15, 20, 25)


def func_with_kwargs(**kwargs):
    print(kwargs)


def combined(*args, **kwargs):
    print(args)
    print(kwargs)


func_with_kwargs(arg1=123, arg2="some arg")
# функция которая ждет любых аргументов которые имеют имя и значение а не только объявленных в функции
# тут будет не tuple на выходе а dict (принимает любые именованные значения) в этом прикол **kwargs


combined(1, 2, 3, 4, 5, arg1=123)
# позиционные попадут в *args, именованные попадут в **kwargs (таким образом можно комбинировать)
# в функциях с **kwargs ключи - это всегда "str" (ограничение отличающее от словаря)

# звездочка у args и kwargs позволяет разворачивать наши какие-то переменные
t = (1, 2)
print(t)

t, tt = (1, 2) # перестает быть tuple и каждому значению присваивается по переменной
print(t, tt)

# t, tt = (1, 2, 3, 4) -- тут будет ругаться так как 4 значения пытаемся присвоить в 2 переменные
# print(t, tt)

t, *tt = (1, 2, 3, 4) # а вот если звездочку поставим то все отлично развернется и у второй переменной будут остальные значения списком
print(t, tt)


l = [1, 2, 3]
ll = [4, 5, 6]

print(l + ll) # объединяет 2 списка в один список
print([l, ll]) # создает список с двумя списками внутри
print([*l, *ll]) # с помощью звездочки мы можем развернуть эти списки внутри списка и будет один список


# Возвращаем несколько значений

def login_password():
    return "login", "password"


l_p = login_password()
print(l_p) # так это будет tuple

l_p = login_password()
login, password = login_password()
print(login, password) # так это будут отдельные значения, т.е. мы развернули этот tuple


# Функция тоже объект

p = print

p(1, 2, 3, 4)

users = [
    {'name': "Oleg", "age": 32},
    {'name': "Sergey", "age": 24},
    {'name': "Stanislav", "age": 15},
    {'name': "Olga", "age": 45},
    {'name': "Maria", "age": 18},
]

def get_user_age(user):
    return user["age"]


print(get_user_age(users[0]))


# Сортировка по возрасту

users.sort(key=get_user_age, reverse=True) # передали написанную функцию в функцию сорт чтобы сравнить значения в
# словаре и отсортировать, ибо если просто пытаться сортировать мы не сможем сравнить значения ключей и значений из
# словаря, reverse естественно меняет сортировку.
print(users)

users.sort(key=lambda user: user["age"]) # это вместо объявления функции 165-166 строк, lambda это анонимная функция,
# user - это аргумент который придет в эту функцию а дальше без return это будет значение которое придет в функцию
print(users)
