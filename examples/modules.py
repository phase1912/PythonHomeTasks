# main.py
import mymodule

print(mymodule.say_hello("World"))

#############

# main.py
from mymodule import say_hello

print(say_hello("World"))

#############

# main.py
from mymodule import say_hello as greeting

print(greeting("World"))

###############

# main.py
from mymodule import say_hello as greeting

print(dir())
print(greeting("World"))

###########

def say_hello(name):
    print(f'Hello, {name}')

print("You imported hello.py")
say_hello('user')

############

# main.py
from mymodule import say_hello as greeting

print(greeting("World"))

#############

def say_hello(name):
    print(f'Hello, {name}')

if __name__ == '__main__':
    print("You imported hello.py")
    say_hello('user')

################

def say_hello(name):
    print(f'Hello {name}')

def main():
    print("You imported hello.py")
    say_hello('user')

if __name__ == '__main__':
    main()

#################

import sys
import os

print(sys.modules["os"])

############

import sys
import os

print(sys.modules.keys())

###############

import sys
import os

print(sys.builtin_module_names)

###########

import sys

for arg in sys.argv:
    print(arg)

 python echo.py test --user -hello some text

##############

import sys

def main():
    if len(sys.argv) > 1:
        print(sys.argv[1])

if __name__ == "__main__":
    main()

 python arg.py 123 

###############

from calculations import salary_calculations

salary = 1000
bonus = 15
salary_with_bonus = salary_calculations.add_bonus(salary, bonus)
print(salary_with_bonus)  # 1015

#################

from calculations.salary_calculations import add_bonus

salary = 1000
bonus = 15
salary_with_bonus = add_bonus(salary, bonus)
print(salary_with_bonus)  # 1015

#########################

import random
import pathlib

current_dir = pathlib.Path(__file__).parent

def get_random_joke():
    try:
        with open(current_dir / "jokes.txt", "r", encoding="utf-8") as file:
            jokes = file.readlines()
            return random.choice(jokes).strip()
    except FileNotFoundError:
        return "Не вдалося знайти файл з анекдотами."


#--------------------

from .jokes_handler import get_random_joke

#---------

from joke import get_random_joke

def main():
    name = input("Будь ласка, введіть ваше ім'я: ")
    print(f"Привіт, {name}!")

    while True:
        user_response = input(f"{name}, бажаєте почути анекдот? (так/ні): ").lower()
        if user_response == "так":
            print(get_random_joke())
        elif user_response == "ні":
            print(f"До побачення, {name}!")
            break

if __name__ == "__main__":
    main()


#############

python -m venv .venv

.\.venv\Scripts\Activate.ps1

pip install package_name

###############

from colorama import Fore

def log_info(message):
    print(f"{Fore.BLUE} [INFO] {Fore.RESET} {message}")

def log_warning(message):
    print(f"{Fore.YELLOW} [WARNING] {Fore.RESET} {message}")

def log_error(message):
    print(f"{Fore.RED} [ERROR] {Fore.RESET} {message}")


#------

import math
from log import log_info, log_warning, log_error

def calculate_square_root(numbers: list) -> None:
    for number in numbers:
        try:
            if number < 0:
                # Логування попередження для від'ємних чисел
                log_warning(f"Знайдено від'ємне число: {number}. Пропускаємо.")
                continue

            root = math.sqrt(number)
            log_info(f"Квадратний корінь з {number} - {root:.2f}")

        except Exception as e:
            # Логування помилки у випадку інших винятків
            log_error(f"Помилка при обчисленні кореня для {number}: {e}")

if __name__ == "__main__":
    # Припустимо, у нас є список чисел
    numbers = [16, -4, 9, 25, 0, 4, "16"]
    calculate_square_root(numbers)

#########

pip freeze > requirements.txt

pip install -r requirements.txt

###########

def is_palindrome(s: str) -> bool:
    new_s = ""
    for char in s:
        if char.isalnum():
            new_s += char.lower()

    s = new_s


length = len(s)
for i in range(length // 2):
    if s[i] != s[length - i - 1]:
        return False
return True

# Використання функції
print(is_palindrome("Козак з казок"))  # Виведе: True

###
new_s = ""
for char in s:
    if char.isalnum():
        new_s += char.lower()

s = new_s

####

for i in range(length // 2):
    if s[i] != s[length - i - 1]:
        return False

##########

def is_palindrome(s: str) -> bool:
    new_s = ""
    for char in s:
        if char.isalnum():
            new_s += char.lower()

    s = new_s
    return s == s[::-1]

# Використання функції
print(is_palindrome("Козак з казок"))  # Виведе: True
