from collections import UserDict
from datetime import datetime, timedelta

from custom_exceptions import InputException
from custom_exceptions import RecordNotFountException


class AddressBook(UserDict):
    def add_record(self, value):
        if not value:
            raise InputException("Invalid data")

        if self.__is_contact_exists(value.name.value):
            raise InputException("Contact has already exists")

        self.add_key(value.name.value, value)

    def add_key(self, key, value):
        self.data[key] = value

    def find(self, key):
        if not self.__is_contact_exists(key):
            raise RecordNotFountException("Couldn't find this contact.")

        return self.data.get(key)

    def remove(self, key):
        if not self.__is_contact_exists(key):
            raise RecordNotFountException("Couldn't remove this contact. Record not exists")

        del self.data[key]

    def get_upcoming_birthdays(self):
        try:
            result = []

            if len(self.data) == 0:
                raise InputException("No upcoming birthdays.")

            current_date = datetime.today().date()
            date_up_to7_days = current_date + timedelta(days=7)

            for key in self.data:
                user = self.data[key]
                if user.birthday is not None:
                    user_birthday = user.birthday.value.date()
                    user_birthday_current_year = datetime(year=current_date.year, month=user_birthday.month,
                                                          day=user_birthday.day).date()

                    if (current_date.month == user_birthday_current_year.month
                            and current_date.day <= user_birthday_current_year.day
                            and current_date.day < date_up_to7_days.day):
                        if user_birthday_current_year.isoweekday() == 6:
                            user_birthday_current_year = user_birthday_current_year + timedelta(days=2)

                        if user_birthday_current_year.isoweekday() == 7:
                            user_birthday_current_year = user_birthday_current_year + timedelta(days=1)

                        result.append(
                            {"name": user.name,
                             "congratulation_date": user_birthday_current_year.strftime("%Y.%m.%d")})

        except ValueError:
            raise ValueError("general error")
        else:
            return f"upcoming birthdays:\n {self.__convert_to_string(result) if len(result) > 0 else 'no upcoming birthdays'}"

    def __is_contact_exists(self, key) -> bool:
        return key in self.data

    @staticmethod
    def __convert_to_string(data):
        return "\n".join(
            f"Name: {entry['name']}, Congratulation date: {entry['congratulation_date']}"
            for entry in data
        )