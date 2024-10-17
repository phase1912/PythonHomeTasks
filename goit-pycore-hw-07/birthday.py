import re
from datetime import datetime

from examples.test import value
from field import Field
from custom_exceptions import InputException


class Birthday(Field):
    def __init__(self, value):
        super().__init__(self.__convert_to_datetime(value))

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")

    def __convert_to_datetime(self, value):
        try:
            pattern = r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})$"

            if not re.match(pattern, value):
                raise InputException

            date = datetime.strptime(value, '%d.%m.%Y')

            return date
        except InputException:
            raise InputException("Invalid date format. Use DD.MM.YYYY")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")