def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid count of arguments."

    name, phone = args

    if is_contact_exists(name, contacts):
        return "Contact has already exists."

    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid count of arguments."

    name, phone = args

    if not is_contact_exists(name, contacts):
        return "Couldn't find this contact."

    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid count of arguments."

    name, = args

    if not is_contact_exists(name, contacts):
        return "Couldn't find this contact."

    return f"Phone: {contacts[name]}"

def show_all(contacts):
    return str(contacts) if len(contacts) > 0 else "Empty list"

def is_contact_exists(key, contacts) -> bool:
    return key in contacts

def main():
    contacts = {}
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
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
