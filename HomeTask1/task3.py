import re

# functions

def normalize_phone(phone_number):
    try:
        phone_number = re.sub(r"[^0-9+]", "", phone_number)

        if not phone_number.startswith("38") and not phone_number.startswith("+"):
            phone_number = f"38{phone_number}"

        if "+" not in phone_number:
            phone_number = f"+{phone_number}"

    except:
        return ""
    else:
        return phone_number

# main code

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)