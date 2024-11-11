from collections import UserDict
from datetime import datetime, timedelta

from .constants import DATE_FORMAT

from .record import Record
from .saveable import Saveable

from .custom_exceptions import InputException
from .custom_exceptions import RecordNotFountException


class AddressBook(UserDict[str, Record], Saveable):
    def __init__(self):
        super().__init__()
        Saveable.__init__(self, filename="addressbook.dat")

    def add_record(self, record: Record):
        if not record:
            raise InputException("Invalid data")

        if self.__is_contact_exists(record.name.value):
            raise InputException("Contact has already exists")

        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        if not self.__is_contact_exists(name):
            raise RecordNotFountException("Couldn't find this contact.")

        return self.data[name]

    def remove(self, name: str):
        if not self.__is_contact_exists(name):
            raise RecordNotFountException(
                "Couldn't remove this contact. Record not exists"
            )

        del self.data[name]

    def get_upcoming_birthdays(self, days):
        current_date = datetime.today().date()  # Це тип date
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday:
                # Перетворюємо на date, щоб уникнути помилки порівняння
                birthday_this_year = record.birthday.value.replace(
                    year=current_date.year
                ).date()

                # Якщо день народження вже пройшов цього року, беремо наступний рік
                if birthday_this_year < current_date:
                    birthday_this_year = birthday_this_year.replace(
                        year=current_date.year + 1
                    )

                # Різниця в днях між поточною датою і днем народження
                difference_days = (birthday_this_year - current_date).days

                # Ініціюємо congratulation_date
                congratulation_date = None

                # Якщо день народження на наступному тижні (включаючи сьогодні)
                if 0 <= difference_days <= days:
                    congratulation_date = birthday_this_year

                    # Якщо день народження випадає на вихідні
                    if congratulation_date.weekday() == 5:  # Субота
                        congratulation_date += timedelta(days=2)
                    elif congratulation_date.weekday() == 6:  # Неділя
                        congratulation_date += timedelta(days=1)

                    # Додаємо до списку
                    upcoming_birthdays.append((record, congratulation_date))
        return upcoming_birthdays

    def __is_contact_exists(self, key) -> bool:
        return key in self.data
