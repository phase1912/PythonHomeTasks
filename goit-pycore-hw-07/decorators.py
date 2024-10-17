from custom_exceptions import InputException, RecordNotFountException

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (InputException, RecordNotFountException) as e:
            return f"{e}"
        except ValueError as e:
            return f"{e}"
        except KeyError as e:
            return f"{e}"
        except IndexError as e:
            return f"{e}"

    return inner