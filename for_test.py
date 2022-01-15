import json

def add(book):
    name = input('Enter name')
    surname = input('Enter surname')
    number = input('Enter number')
    city = input('Enter city')
    new = {
        'name': name,
        'number': number,
        'surname': surname,
        'city': city
    }
    book.append(new)
    with open('js_file.json', 'w') as file:
        json.dump(book, file, indent=4)
    return book


def search(book):
    ent = input('What is search?:[N]ame,[S]urname,[P]hone number,[C]ity,[E]xit').lower()
    if ent == 'n':
        name = input('Enter name').capitalize()
        for contakt in book:
            if contakt['name'] == name:
                print(contakt['name'], contakt['surname'], contakt['number'], contakt['city'])
                option = input('Enter option: [R]enew, [D]elete,[E]xit').lower()
                if option == 'r':
                    del contakt['name']
                    del contakt['surname']
                    del contakt['number']
                    del contakt['city']
                    with open('js_file.json', 'w') as js_file:
                        json.dump(book, js_file, indent=4)
                    renew(book)
                if option == 'e':
                    break
                if option == 'd':
                    del contakt['name']
                    del contakt['surname']
                    del contakt['number']
                    del contakt['city']
                    with open('js_file.json', 'w') as js_file:
                        json.dump(book, js_file, indent=4)
                    with open('js_file.json', 'r') as js_file:
                        json.load(js_file)
                        print(js_file)
    elif ent == 's':
        surname = input('Enter surname').capitalize()
        for contakt in book:
            if contakt['surname'] == surname:
                print(contakt['name'], contakt['surname'], contakt['number'], contakt['city'])
                option = input('Enter option: [R]enew, [D]elete,[E]xit').lower()
                if option == 'r':
                    del contakt['name']
                    del contakt['surname']
                    del contakt['number']
                    del contakt['city']
                    with open('js_file.json', 'w') as js_file:
                        json.dump(book, js_file, indent=4)
                    renew(book)
                if option == 'e':
                    break
                if option == 'd':
                    del contakt['name']
                    del contakt['surname']
                    del contakt['number']
                    del contakt['city']
                    with open('js_file.json', 'w') as js_file:
                        json.dump(book, js_file, indent=4)
                    with open('js_file.json', 'r') as js_file:
                        json.load(js_file)
                        print(js_file)
    elif ent == 'p':
        number = input('Enter number')
        for contakt in book:
            if contakt['number'] == number:
                print(contakt['name'], contakt['surname'], contakt['number'], contakt['city'])
                option = input('Enter option: [R]enew, [D]elete,[E]xit').lower()
                if option == 'r':
                    del contakt['name']
                    del contakt['surname']
                    del contakt['number']
                    del contakt['city']
                    with open('js_file.json', 'w') as js_file:
                        json.dump(book, js_file, indent=4)
                    renew(book)
                if option == 'e':
                    break
                if option == 'd':
                    del contakt['name']
                    del contakt['surname']
                    del contakt['number']
                    del contakt['city']
                    with open('js_file.json', 'w') as js_file:
                        json.dump(book, js_file, indent=4)
                    with open('js_file.json', 'r') as js_file:
                        json.load(js_file)
                        print(js_file)
    elif ent == 'c':
        city = input('Enter city').capitalize()
        for contakt in book:
            if contakt['city'] == city:
                print(contakt['name'], contakt['surname'], contakt['number'], contakt['city'])
                option = input('Enter option: [R]enew, [D]elete,[E]xit').lower()
                if option == 'r':
                    del contakt['name']
                    del contakt['surname']
                    del contakt['number']
                    del contakt['city']
                    with open('js_file.json', 'w') as js_file:
                        json.dump(book, js_file, indent=4)
                    renew(book)
                if option == 'e':
                    break
                if option == 'd':
                    del contakt['name']
                    del contakt['surname']
                    del contakt['number']
                    del contakt['city']
                    with open('js_file.json', 'w') as js_file:
                        json.dump(book, js_file, indent=4)
                    with open('js_file.json', 'r') as js_file:
                        json.load(js_file)
                        print(js_file)
    elif ent == 'e':
        exit()


def renew(book):

    name = input('Enter new name')
    surname = input('Enter new surname')
    number = input('Enter new number')
    city = input('Enter new city')
    new = {
        'name': name,
        'number': number,
        'surname': surname,
        'city': city
    }
    book.append(new)
    with open('js_file.json', 'w') as file:
        json.dump(book, file, indent=4)
    return book


if __name__ == '__main__':

    book = [{'name': 'Ivan', 'surname': 'Prokopenko', 'number': '+6475896743', 'city': 'Kyiv'}]
    with open('js_file.json', 'w') as file:
        json.dump(book, file, indent=4)
    while True:
        option = input('Enter option: [A]dd;[S]earch;[Q]uit ').lower()
        if option == 'a':
            add(book)
            with open('js_file.json', 'r') as file:
                a = json.load(file)
                print(a)
        elif option == 's':
            search(book)
        elif option == 'q':
            exit()