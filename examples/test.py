


# x = int(input('Введіть число: '))
#
# if x % 2 == 0:
#     print("Число x є парним.")
# else:
#     print("Число x є непарним.")

# num = int(input("Введіть число: "))
#
# length = len(str(num))
#
# if length == 2 and num % 2 == 0:
#     print("Парне двозначне число")
# else:
#     print("Ні")

# Задаємо конкретне число
# num = int(input())
#
# # Перевіряємо кратність
# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)
##################
# x = int(input("X: "))
# y = int(input("Y: "))
#
# if x >= 0:
#     if y >= 0:  # x > 0, y > 0
#         print("Перша чверть")
#     else:  # x > 0, y < 0
#         print("Четверта чверть")
# else:
#     if y >= 0:  # x < 0, y > 0
#         print("Друга чверть")
#     else:  # x < 0, y < 0
#         print("Третя чверть")
###########################
is_nice = True
state = "nice" if is_nice else "not nice"
##############
some_data = None
msg = some_data or "Не було повернено даних"
#######################
# point = (1, 0)
#
# match point:
#     case (0, 0):
#         print("Точка в центрі координат")
#     case (0, y):
#         print(f"Точка лежить на осі Y: y={y}")
#     case (x, 0):
#         print(f"Точка лежить на осі X: x={x}")
#     case (x, y):
#         print(f"Точка має координати:  x={x}, y={y}")
#     case _:
#         print("Це не точка")
################################
# pets = ["dog", "fish", "cat"]
#
# match pets:
#     case ["dog", "cat", _]:
#         # Випадок, коли є і собака, і кіт
#         print("There's a dog and a cat.")
#     case ["dog", _, _]:
#         # Випадок, коли є тільки собака
#         print("There's a dog.")
#     case _:
#         # Випадок для інших комбінацій
#         print("No dogs.")
##########################
# fruit = 'apple'
# for char in fruit:
#     print(char)
###################
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for char in alphabet:
#     print(char, end=" ")
#####################
# Зчитування рядка від користувача
# user_input = input("Введіть рядок: ")
#
# # Ініціалізація змінних для підрахунку символів та пробілів
# total_chars = len(user_input)  # загальна кількість символів у рядку
# space_count = 0  # кількість пробілів
#
# # Підрахунок кількості пробілів
# for char in user_input:
#     if char == " ":
#         space_count += 1
#
# # Виведення результатів
# print(f"Загальна кількість символів у рядку: {total_chars}")
# print(f"Кількість пробілів у рядку: {space_count}")
###########################
# a = 0
# while True:
#     print(a)
#     if a >= 20:
#         break
#     a = a + 1
###########
for i in range(0, 10, 2):
    print(i)

some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)

list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']

for number, letter in zip(list1, list2):
    print(number, letter)

numbers = {
    1: "one",
    2: "two",
    3: "three"
}

for key in numbers:
    print(key)

for key in numbers.keys():
    print(key)

for val in numbers.values():
    print(val)

for key, value in numbers.items():
    print(key, value)
#####################
# val = 'a'
# try:
#     val = int(val)
# except ValueError:
#     print(f"val {val} is not a number")
# else:
#     print(val > 0)
# finally:
#     print("This will be printed anyway")
######################
# age = input("How old are you? ")
# try:
#     age = int(age)
#     if age >= 18:
#         print("You are adult.")
#     else:
#         print("You are infant")
# except ValueError:
#     print(f"{age} is not a number")
#####################
# def print_max(a: int, b: int):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'дорівнює', b)
#     else:
#         print(b, 'максимально')
#
# print_max(3, 4)  # пряма передача значень
#
# x = 5
# y = 7
# print_max(x, y)  # передача змінних у якості аргументів
##########
# def my_function() -> ReturnType:
#     # виконати дії
#     return result
###########
# def modify_list(lst: list) -> None:
#     lst = lst.copy()
#     lst.append(4)
#
# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # виведе: [1, 2, 3]
################
# def string_to_codes(string: str) -> dict:
#     # Ініціалізація словника для зберігання кодів
#     codes = {}
#     # Перебір кожного символу в рядку
#     for ch in string:
#         # Перевірка, чи символ вже є в словнику
#         if ch not in codes:
#             # Додавання пари символ-код в словник
#             codes[ch] = ord(ch)
#     return codes
###############
#def greet(name, message="Привіт"):
#     print(f"{message}, {name}!")
# використовує значення за замовчуванням для message
# greet("Олексій")
#
# # передача власного значення для message
# greet("Марія", message="Добрий день")
##########
# def func(a, b=5, c=10):
#     print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)
#
# # a дорівнює 3, b дорівнює 7, а c дорівнює 10
# func(3, 7)
#
# # a дорівнює 25, b дорівнює 5, а c дорівнює 24
# func(25, c=24)
#
# # a дорівнює 100, b дорівнює 5, а c дорівнює 50
# func(c=50, a=100)
##########
# def print_all_args(*args):
#     for arg in args:
#         print(arg)
#
# print_all_args(1, 'hello', True)
#################
# def concatenate(*args) -> str:
#     result = ""
#     for arg in args:
#         result += arg
#     return result
#
# print(concatenate("Hello", " ", "world", "!"))
######################
# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# greet(name="Alice", age=25)
###############
# def example_function(*args, **kwargs):
#     print("Позиційні аргументи:", args)
#     print("Ключові аргументи:", kwargs)
#
# example_function(1, 2, 3, name="Alice", age=25)
############
# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")
#
# person_info = {"name": "Alice", "age": 25}
# greet(**person_info)
#################
# def factorial(n):
#     print("Виклик функції factorial з n = ", n)
#     if n == 1:
#         print("Базовий випадок, n = 1, повернення 1")
#         return 1
#     else:
#         result = n * factorial(n-1)
#         print("Повернення результату для n = ", n, ": ", result)
#         return result
#
# print(factorial(5))

##################
# # Один мільйон
# a = 1_000_000
# print(a)  # Виведе 1000000
#
# # Десять мільйонів
# b = 10_000_000
# print(b)  # Виведе 10000000
#
# # Один мільярд
# c = 1_000_000_000
# print(c)  # Виведе 1000000000
###########
# import random
#
# dice_roll = random.randint(1, 6)
# print(f"Ви кинули {dice_roll}")
############
# import random
#
# fill_percentage = random.random() * 100
# print(f"Заповнення: {fill_percentage:.2f}%")
#########
# import random
#
# target = random.randrange(1, 11, 2)
# print(f"Ціль: {target}")
##########
# import random
#
# cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]
#
# random.shuffle(cards)
#
# print(f"Перемішана колода: {cards}")
#############
import random

fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))
########
import random

numbers = [1, 2, 3, 4, 5]
chosen_numbers = random.choices(numbers, k=3)
print(chosen_numbers)
#############
import random

colors = ['червоний', 'зелений', 'синій']
weights = [10, 1, 1]
chosen_color = random.choices(colors, weights, k=1)
print(chosen_color)
############
# import random
#
# participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
# team = random.sample(participants, 4)
# print(f"Команда: {team}")
################
import math

# Вихідне число
x = 3.7

# Використання різних методів округлення
ceil_result = math.ceil(x)  # Округлення вгору
floor_result = math.floor(x)  # Округлення вниз
trunc_result = math.trunc(x)  # Відсікання дробової частини

print(ceil_result, floor_result, trunc_result)
##############
import math

# Використання констант
print(math.pi)  # Виведе приблизне значення π

# Тригонометрія
angle = math.radians(60)  # Конвертація з градусів у радіани
print(math.sin(angle))  # Синус кута

# Корінь числа
print(math.sqrt(9))  # Квадратний корінь з 9

# Логарифми
print(math.log(10, 2))  # Логарифм 10 за основою 2
############
import math

r = math.isclose(0.1 + 0.2, 0.3)
print(r)  # Це поверне True