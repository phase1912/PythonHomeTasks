from collections import UserDict
from custom_exceptions import InputException
from custom_exceptions import RecordNotFountException


class AddressBook(UserDict):
    def add_record(self, value):
        if not value:
            raise InputException("Invalid data")

        if self.is_contact_exists(value.name.value):
            raise InputException("Contact has already exists")

        self.add_key(value.name.value, value)

    def add_key(self, key, value):
        self.data[key] = value

    def find(self, key):
        if not self.is_contact_exists(key):
            raise RecordNotFountException("Couldn't find this contact.")

        return self.data.get(key)

    def remove(self, key):
        if not self.is_contact_exists(key):
            raise RecordNotFountException("Couldn't remove this contact. Record not exists")

        del self.data[key]

    def is_contact_exists(self, key) -> bool:
        return key in self.data