from datetime import datetime

# functions

def get_days_from_today(date):
    try:
        now = datetime.today().date()
        datetime_object = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print(f'input data {date} does not match format patern YYYY-MM-DD')
        return None
    except:
        print('general error')
        return None
    else:
        return (now - datetime_object).days

# main code

date_str = input('Input date in format YYYY-MM-DD: ')

result = get_days_from_today(date_str)

if result is None:
    print('Not correct input data')
else:
    print(result)