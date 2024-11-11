from collections import defaultdict
from datetime import datetime

from .constants import DATE_FORMAT
from .decorators import input_error
from .table import print_table
from .address_book import AddressBook
from .notes import Notes
from .note import Note
from .record import Record


@input_error
def add_contact(args, book: AddressBook):
    if len(args) == 0:
        raise ValueError("Give me name and phone please.")

    if len(args) != 2:
        raise IndexError

    name, phone = args

    john_record = Record(name)
    john_record.add_phone(phone)
    book.add_record(john_record)
    book.save_data()
    return "Contact added."


@input_error
def change_phone(args, book: AddressBook):
    if len(args) == 0:
        raise ValueError("Give me name and phones please.")

    if len(args) != 3:
        raise IndexError

    name, old_phone, new_phone = args

    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    book.save_data()

    return "Phone changed."


@input_error
def add_phone(args, book: AddressBook):
    if len(args) == 0:
        raise ValueError("Give me name and phone please.")

    if len(args) != 2:
        raise IndexError

    name, phone = args

    record = book.find(name)
    record.add_phone(phone)
    book.save_data()

    return "Phone added."


@input_error
def all_contacts(book: AddressBook):
    if len(book.data):
        print_contacts_table(book.data.values())
    else:
        print("Empty list")


def print_contacts_table(records: list[Record]):
    if not len(records):
        return
    title = "Contacts:" if 1 < len(records) else ""
    fields = ["Contact name", "Email", "Birthday", "Phones"]
    rows = [get_contact_row(record) for record in records]
    print_table(title, fields, rows, hrules=True)


def get_contact_row(record: Record) -> list[str]:
    return [
        str(record.name),
        "" if record.email is None else str(record.email),
        "" if record.birthday is None else str(record.birthday),
        "\n".join(p.value for p in record.phones),
    ]


@input_error
def remove_phone(args, book: AddressBook):
    if len(args) == 0:
        raise ValueError("Give me name and phone please.")

    if len(args) != 2:
        raise IndexError

    name, phone = args

    record = book.find(name)
    record.remove_phone(phone)
    book.save_data()

    return "Phone removed."


@input_error
def add_birthday(args, book: AddressBook):
    if len(args) == 0:
        raise ValueError("Give me name and birthday please.")

    if len(args) != 2:
        raise IndexError

    name, birthday = args

    record = book.find(name)
    record.add_birthday(birthday)
    book.save_data()

    return "Birthday added."


@input_error
def add_email(args, book: AddressBook):
    if len(args) == 0:
        raise ValueError("Give me name and email please.")

    if len(args) != 2:
        raise IndexError

    name, email = args

    record = book.find(name)
    record.add_email(email)
    book.save_data()

    return "Email added."


@input_error
def edit_email(args, book: AddressBook):
    if len(args) == 0:
        raise ValueError("Give me name and email please.")

    if len(args) != 2:
        raise IndexError

    name, email = args

    record = book.find(name)
    record.edit_email(email)
    book.save_data()

    return "Email added."


@input_error
def find_contact(args, book: AddressBook):
    (name,) = args

    record = book.find(name)
    print_contacts_table([record])


@input_error
def remove_contact(args, book: AddressBook):
    (name,) = args

    book.remove(name)
    book.save_data()

    return "Contact removed."


@input_error
def show_birthday(args, book: AddressBook):
    (name,) = args

    record = book.find(name)
    print_table(
        title="",
        fields=["Contact name", "Birthday"],
        rows=[[str(record.name), str(record.birthday)]],
    )


@input_error
def coming_birthdays(args, book):
    if len(args) == 0:
        raise ValueError("Give me numbers of days.")

    if len(args) != 1:
        raise IndexError

    days = int(args[0])
    upcoming_birthdays = book.get_upcoming_birthdays(days)
    if upcoming_birthdays:
        title = "Upcoming birthdays:"
        fields = ["Congratulation date", "Contact name", "Birthday", "Age"]
        congrat_days = defaultdict(list)
        for record, date in upcoming_birthdays:
            congrat_days[date].append(record)

        rows = []
        for date in congrat_days:
            contacts = congrat_days[date]
            row = [
                date.strftime(DATE_FORMAT),
                "\n".join(str(contact.name) for contact in contacts),
                "\n".join(str(contact.birthday) for contact in contacts),
                "\n".join(
                    str((date.year - contact.birthday.value.year) % 365)
                    for contact in contacts
                ),
            ]
            rows.append(row)

        print_table(title, fields, rows, hrules=True)
        # return "\n".join([f"{name}: {date}" for name, date in upcoming_birthdays])
    else:
        return f"No birthdays within the {days} days."


@input_error
def show_phones(args, book: AddressBook):
    (name,) = args

    record = book.find(name)
    print_table(
        title="",
        fields=["Contact name", "Phones"],
        rows=[
            [
                str(record.name),
                f"{'\n'.join(str(phone) for phone in record.get_all_phones())}",
            ]
        ],
    )


@input_error
def add_note(args, notes: Notes):
    if len(args) == 0:
        raise ValueError("Give me title and description please.")

    if len(args) != 2:
        raise IndexError

    title, description = args

    note_id = notes.add(Note(title, description))
    notes.save_data()

    return f"Note added with id: {note_id}"


def print_notes(notes: dict[int, Note], title: str = "Notes:"):
    fields = ["ID", "Title", "Description", "Tags"]
    rows = []
    for record in notes:
        rows.append(
            [
                record,
                notes[record].title,
                notes[record].description,
                "; ".join([tag.value for tag in notes[record].tags]),
            ]
        )
    print_table(title, fields, rows)


@input_error
def all_notes(notes: Notes):
    if len(notes.data):
        print_notes(notes.data)
    else:
        print("Empty list")


@input_error
def edit_note_title(args, notes: Notes):
    if len(args) == 0:
        raise ValueError("Give me id and title please.")

    if len(args) != 2:
        raise IndexError

    id, title = args

    if not id.isdigit():
        raise ValueError("Invalid id.")

    notes.update_title(int(id), title)

    return "Title updated."


@input_error
def edit_note_description(args, notes: Notes):
    if len(args) == 0:
        raise ValueError("Give me id and description please.")

    if len(args) != 2:
        raise IndexError

    id, description = args

    if not id.isdigit():
        raise ValueError("Invalid id.")

    notes.update_description(int(id), description)

    return "Description updated."


@input_error
def remove_note(args, notes: Notes):
    (id,) = args

    if not id.isdigit():
        raise ValueError("Invalid id.")

    notes.remove(int(id))
    notes.save_data()

    return "Note removed."


@input_error
def find_notes_by_text(args, notes: Notes):
    (query,) = args

    result = notes.search_by_text(query)

    if not len(result):
        return "Notes not found."

    print_notes(result)


@input_error
def add_note_tag(args, notes: Notes):
    if len(args) == 0:
        raise ValueError("Give me id and tag please.")

    if len(args) != 2:
        raise ValueError("Invalid count of arguments.")

    id, tag = args

    if not id.isdigit():
        raise ValueError("Invalid id.")

    notes.add_note_tag(int(id), tag)

    return "Tag added."


@input_error
def remove_note_tag(args, notes: Notes):
    if len(args) == 0:
        raise ValueError("Give me id and tag please.")

    if len(args) != 2:
        raise ValueError("Invalid count of arguments.")

    id, tag = args

    if not id.isdigit():
        raise ValueError("Invalid id.")

    notes.remove_note_tag(int(id), tag)
    notes.save_data()

    return "Tag removed."


@input_error
def find_notes_by_tag(args, notes: Notes):
    if len(args) != 1:
        raise ValueError("Invalid count of arguments.")

    (tag,) = args

    result = notes.search_by_tag(tag)

    if not len(result):
        return "Notes not found."

    print_notes(result)
