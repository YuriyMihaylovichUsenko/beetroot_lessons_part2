import json
import mypy


def start_and_open(file_name) -> dict[str, str] | None:
    opening_object_name: str = input(
        'What do you want to open? Input '
        'filename(phone_book.json) (Press q for exit)')

    if opening_object_name == 'q':
        exit()
    elif opening_object_name == 'phone_book.json':
        with open(file_name, 'r') as f:
            data: dict[str, str] = json.load(f)
        return data
    else:
        raise FileNotFoundError('object is not found')


def dump_and_exit(data) -> None:
    with open('phone_book.json', 'w') as file:
        json.dump(data, file, indent=4)
    exit()


def add_contacts(data) -> None:
    input_surname: str = input('input surname (Press q for exit): ')
    if input_surname == 'q':
        dump_and_exit(data)

    input_name: str = input('input name (Press q for exit): ')
    if input_name == 'q':
        dump_and_exit(data)

    input_town: str = input('input town (Press q for exit): ')
    if input_town == 'q':
        dump_and_exit(data)

    input_number: str = input('input number (Press q for exit): ')
    if input_number == 'q':
        dump_and_exit(data)

    entry: dict[str, str] = {'first_name': input_name,
                             'last_name': input_surname,
                             'town': input_town, 'number': input_number}

    data.append(entry)

    print(f'{entry} is added to phone book')


def search_by_first_name(data) -> str | None | list[dict[str, str]]:
    input_name: str = input('input name (Press q for exit): ')
    if input_name == 'q':
        dump_and_exit(data)
    if input_name not in (i['first_name'] for i in data):
        return f'there is not contacts with name {input_name} in the phone book'
    else:
        return [i for i in data if i['first_name'] == input_name]


def search_by_last_name(data) -> None:
    input_surname: str = input('input surname (Press q for exit): ')
    if input_surname == 'q':
        dump_and_exit(data)
    if input_surname not in (i['last_name'] for i in data):
        print(f'there are not contacts with name {input_surname} '
              f'in the phone book')
    else:
        print([i for i in data if i['last_name'] == input_surname])


def search_by_town(data) -> None:
    input_town: str = input('input town (Press q for exit): ')
    if input_town == 'q':
        dump_and_exit(data)
    if input_town not in (i['town'] for i in data):
        print(f'there is not contacts with name {input_town} in the phone book')
    else:
        print([i for i in data if i['town'] == input_town])


def search_by_number(data) -> None:
    input_number: str = input('input number (Press q for exit): ')
    if input_number == 'q':
        dump_and_exit(data)
    elif input_number not in (i['number'] for i in data):
        print(f'there is not contacts with name {input_number} '
              f'in the phone book')
    else:
        print([i for i in data if i['number'] == input_number])


def del_entry_by_number(data) -> None:
    input_number: str = input('input number (Press q for exit): ')
    if input_number == 'q':
        dump_and_exit(data)
    if input_number not in (i['number'] for i in data):
        print(f'there is not contacts with name {input_number} '
              f'in the phone book')
    else:
        removing_entry: list[dict[str, str]] = [i for i in data if i['number'] == input_number]
        confirm_removing: str = input(f'This contacts will be removed '
                                 f'{removing_entry}. Ok?: (Press q for exit)')
        if confirm_removing == 'q':
            dump_and_exit(data)
        elif confirm_removing == 'ok':
            for i in removing_entry:
                data.remove(i)
        print('The contact has removed')


def edit_entry_by_number(data) -> None:
    input_number: str = input('input number (Press q for exit): ')
    if input_number == 'q':
        dump_and_exit(data)
    if input_number not in (i['number'] for i in data):
        print(f'there is not contacts with name {input_number} '
              f'in the phone book')
    for i in data:
        if i['number'] == input_number:
            editing_entry: str = i
            print(editing_entry)
            key_for_editing: str = input('What do you wont to edit? '
                                    'surname/name/patronymic/town/number? '
                                    '(Press q for exit)')
            if key_for_editing == 'q':
                dump_and_exit(data)
            new_value_for_key_for_editing: str = input(
                'Input new value for ' + key_for_editing + '(Press q for exit)')
            if new_value_for_key_for_editing == 'q':
                dump_and_exit(data)
            i[key_for_editing] = new_value_for_key_for_editing
            print(f'Now it looks like  {i}')


def function_choice(data):
    function_dict: dict[str, ...] = {'1': add_contacts,
                     '2': search_by_first_name,
                     '3': search_by_last_name,
                     '5': search_by_number,
                     '6': search_by_town,
                     '7': del_entry_by_number,
                     '8': edit_entry_by_number,
                     '9': dump_and_exit}

    while True:
        function_choice_: str = input('\nWhat do you want to do:\n'
                                 'Add new entries - press 1\n'
                                 'Search by first name - press 2\n'
                                 'Search by last name - press 3\n'
                                 'Search by telephone number - press 5\n'
                                 'Search by city - press 6\n'
                                 'Delete a record for a given telephone'
                                 ' number - press 7\n'
                                 'Update a record for a given telephone'
                                 ' number - press 8\n'
                                 'To exit the program - press 9\n')
        function = function_dict.get(function_choice_)
        if function:
            function(data)
        else:
            print('Your input is wrong')


def phone_book(book):
    data: dict[str, str] = start_and_open(book)
    function_choice(data)


def main():
    phone_book('phone_book.json')


if __name__ == '__main__':
    main()
