def total_salary(path):
    total = 0
    average = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            items = file.readlines()

            try:
                count = 0

                for item in items:
                    try:
                        name, salary = item.split(',')

                        if name is not None and name != '' and salary is not None and salary != '':
                            total += float(salary)
                            count += 1

                    except ValueError:
                        continue

                if total > 0:
                    average = total / count
            except:
                print('general error')
                return 0, 0

    except FileNotFoundError:
        print(f'file with path: {path} not found')
    except:
        print('general error')

    return total, average

total, average = total_salary("salary_file.txt")

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")