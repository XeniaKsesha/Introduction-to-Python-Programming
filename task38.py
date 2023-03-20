
# функция для открытия телефонного справочника
def open_phonebook():
        with open('phonebook.txt', 'r') as f:
            f.read()

# функция для сохранения телефонного справочника в файл
def save_phonebook(phonebook):
    with open('phonebook.txt', 'w') as f:
        for name, phone in phonebook.items():
            f.write(f"{name},{phone}\n")
    print('Телефонный справочник сохранен')

# функция для вывода всех контактов из телефонного справочника
def show_all_contacts(phonebook):
    print('Контакты в телефонном справочнике: ')
    for name, phone in phonebook():
        print(f"{name}: {phone}")

# функция для поиска контакта по имени
def find_contact(phonebook):
    name = input('Введите имя контакта: ')
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print('Контакт не найден')

# функция для добавления нового контакта
def add_contact(phonebook):
    name = input('Введите имя нового контакта: ')
    number = input('Введите номер телефона нового контакта: ')
    phonebook[name] = number
    print('Контакт добавлен')

# функция для изменения контакта
def edit_contact(phonebook):
    name = input('Введите имя контакта, который нужно изменить: ')
    if name in phonebook:
        new_phone_number = input('Введите новый номер телефона контакта: ')
        phonebook[name] = new_phone_number
        print('Контакт успешно изменен')
    else:
        print('Контакт не найден')

# функция удаления контакта
def delete_contact(phonebook):
    name = input('Введите имя контакта, который нужно удалить: ')
    if name in phonebook():
            del phonebook[name]
            print(f'Контакт (name) успешно удален')
    else:
        print('Контакт не существует')

# функция закрытия телефонного справочника
def exit_phonebook():
    print("Выход из телефонной книги")
    exit()

