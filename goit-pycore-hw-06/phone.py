from field import Field
from custom_exceptions import InputException
import re

class Phone(Field):
    def __init__(self, value):
        if not self.is_valid_phone_number(value):
            raise InputException("Phone not valid")

        super().__init__(value)

    @staticmethod
    def is_valid_phone_number(phone):
        pattern = r"^\d{10}$"
        return bool(re.match(pattern, phone))