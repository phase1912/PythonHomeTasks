def get_cats_info(path):
    result = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            items = file.readlines()

            try:
                for item in items:
                    try:
                        id, name, age = item.replace('\n', '').split(',')

                        if name is not None and name != '' and id is not None and id != '':
                            result.append({ 'id': id, 'name': name, 'age': age })

                    except ValueError:
                        continue

            except:
                print('general error')
                return []

    except FileNotFoundError:
        print(f'file with path: {path} not found')
    except:
        print('general error')

    return result

cats_info = get_cats_info("cats_file.txt")

print(cats_info)