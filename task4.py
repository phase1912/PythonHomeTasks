from datetime import datetime, timedelta

# functions

def get_upcoming_birthdays(data):
    try:
        result = []

        if len(data) == 0:
            return []

        current_date = datetime.today().date()
        date_up_to7_days = current_date + timedelta(days=7)

        for user in data:
            user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            user_birthday_current_year = datetime(year=current_date.year, month=user_birthday.month, day=user_birthday.day).date()

            if (current_date.month == user_birthday_current_year.month
                    and current_date.day <= user_birthday_current_year.day
                    and current_date.day < date_up_to7_days.day):
                if user_birthday_current_year.isoweekday() == 6:
                    user_birthday_current_year = user_birthday_current_year + timedelta(days=2)


                if user_birthday_current_year.isoweekday() == 7:
                    user_birthday_current_year = user_birthday_current_year + timedelta(days=1)

                result.append({ "name": user["name"], "congratulation_date": user_birthday_current_year.strftime("%Y.%m.%d") })

    except:
        print("general error")
        return []
    else:
        return result

# main code

users = [
    { "name": "John Doe", "birthday": "1985.09.20" },
    { "name": "Jane Smith", "birthday": "1990.09.22" },
    { "name": "Tim Kook", "birthday": "1991.09.16" },
    { "name": "John Cina", "birthday": "1994.09.21" },
    { "name": "Michal Jacson", "birthday": "1995.10.05" },
    { "name": "Michal Raduga", "birthday": "1997.10.10" },
    { "name": "Michal Titarenko", "birthday": "1991.11.11" }
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)