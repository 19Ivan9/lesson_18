from for_test import *
import unittest
import os.path
from unittest.mock import patch

js = 'js_file.json'


class Test(unittest.TestCase):
    """Если всё что написано ниже дичь,
        то в коменнтарии к ДЗ можно написать просто - 'Дичь'
        Я всё пойму и переделаю"""

    def test_func_true(self):
        self.assertTrue(add)
        self.assertTrue(search)
        self.assertTrue(renew)

    def test_file(self):
        # os.path.isfile('js')
        try:
            with open(js, 'r') as js_file:
                json.load(js_file)
        except FileNotFoundError:
            print('File not found!')

    @patch('for_test.input', return_value='a')
    def test_add(self, input):
        book = [{'name': 'Ivan', 'surname': 'Prokopenko', 'number': '+6475896743', 'city': 'Kyiv'}]
        with open(js, 'w') as file:
            json.dump(book, file, indent=4)
        start_len = len(book)
        add(book)
        self.assertTrue(len(book) > start_len)
        self.assertIsInstance(add([]), list)

    @patch('for_test.input', return_value='s')
    def test_search(self, input):
        book = [{'name': 'Ivan', 'surname': 'Prokopenko', 'number': '+6475896743', 'city': 'Kyiv'}]

        def search(book):
            name = 'Ivan'
            for contakt in book:
                if contakt['name'] == name:
                    return contakt['name']

        self.assertIn('Ivan', search(book))
        self.assertIsNone(search([]))

    def test_renew(self):
        book = [{'name': 'Ivan', 'surname': 'Prokopenko', 'number': '+6475896743', 'city': 'Kyiv'}]

        def renew(book):
            new = {'name': 'f', 'number': '4', 'surname': 'e', 'city': 'g'}
            book.append(new)
            with open('js_file.json', 'w') as file:
                json.dump(book, file, indent=4)
            return book

        self.assertIsInstance(renew(book), list)
        self.assertEqual(renew(book), book)


if __name__ == '__main__':
    unittest.main()
