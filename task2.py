import random

# functions

def get_numbers_ticket(min, max, quantity):
    try:
        min = int(min)
        max = int(max)
        quantity = int(quantity)

        if min < 1:
            print(f'min value must be more than {min}')
            return []

        if max > 1000:
            print(f'max value must be less than {max}')
            return []

        values = random.sample(range(min, max), quantity)

        result_values = sorted(values)
    except ValueError:
        print('not correct input numbers')
        return []
    except:
        print('general error')
        return []
    else:
        return result_values

# main code

min = input('input min value(must be more than 1): ')
max = input('input max value(must be less than 1000): ')
quantity = input('input quantity of these unique values: ')

result = get_numbers_ticket(min, max, quantity)

print("Ваші лотерейні числа:", result)