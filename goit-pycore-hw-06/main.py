from address_book import AddressBook
from record import Record
from decorators import input_error

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def show_phones(args, book: AddressBook):
    if len(args) != 1:
        raise ValueError("Invalid count of arguments.")

    name, = args

    record = book.find(name)

    return f"Phones: {'; '.join(p.value for p in record.get_all_phones())}"

@input_error
def find(args, book: AddressBook):
    if len(args) != 1:
        raise ValueError("Invalid count of arguments.")

    name, = args

    record = book.find(name)

    return record

@input_error
def add_contact(args, book: AddressBook):
    if len(args) == 0:
        raise ValueError("Give me name and phone please.")

    if len(args) != 2:
        raise ValueError("Invalid count of arguments.")

    name, phone = args

    john_record = Record(name)
    john_record.add_phone(phone)
    book.add_record(john_record)

    return "Contact added."

@input_error
def change_phone(args, book: AddressBook):
    if len(args) == 0:
        raise ValueError("Give me name and phones please.")

    if len(args) != 3:
        raise ValueError("Invalid count of arguments.")

    name, old_phone, new_phone = args

    record = book.find(name)
    record.edit_phone(old_phone, new_phone)

    return "Phone changed."

@input_error
def add_phone(args, book: AddressBook):
    if len(args) == 0:
        raise ValueError("Give me name and phone please.")

    if len(args) != 2:
        raise ValueError("Invalid count of arguments.")

    name, phone = args

    record = book.find(name)
    record.add_phone(phone)

    return "Phone added."

@input_error
def remove_phone(args, book: AddressBook):
    if len(args) == 0:
        raise ValueError("Give me name and phone please.")

    if len(args) != 2:
        raise ValueError("Invalid count of arguments.")

    name, phone = args

    record = book.find(name)
    record.remove_phone(phone)

    return "Phone added."

def remove_contact(args, book: AddressBook):
    if len(args) != 1:
        raise ValueError("Invalid count of arguments.")

    name, = args

    book.remove(name)

    return "Contact removed."


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change_phone":
            print(change_phone(args, book))
        elif command == "add_phone":
            print(add_phone(args, book))
        elif command == "remove_phone":
            print(add_phone(args, book))
        elif command == "find":
            print(find(args, book))
        elif command == "remove":
            print(remove_contact(args, book))
        elif command == "phones":
            print(show_phones(args, book))
        elif command == "all":
            if len(book.data) > 0:
                print("Contacts:")
                for name, record in book.data.items():
                    print(record)
            else:
                print("Empty list")

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()