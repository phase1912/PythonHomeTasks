from name import Name
from phone import Phone
from custom_exceptions import InputException

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_str: str):
        if self.find_phone(phone_str):
            raise InputException("This phone has already exists for current user")

        phone = Phone(phone_str)

        self.phones.append(phone)

    def edit_phone(self, old_phone: str, new_phone: str):
        phone = self.find_phone(old_phone)

        if not phone:
            raise InputException("This phone not exists for current user")

        self.phones[self.phones.index(phone)] = Phone(new_phone)

    def remove_phone(self, phone_str: str):
        phone = self.find_phone(phone_str)

        if not phone:
            raise InputException("Couldn't remove this phone. Phone not exists for current user")

        self.phones.remove(phone)

    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                return p

        return None

    def get_all_phones(self):
        return self.phones

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"