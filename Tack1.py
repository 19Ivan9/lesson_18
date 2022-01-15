import unittest


class Mathematician:
    def __init__(self):
        pass

    def square_nums(self, arr):
        return [i ** 2 for i in arr]

    def remove_positives(self, arr):
        return [i for i in arr if i < 0]

    def filter_leaps(self, arr):
        return [i for i in arr if i % 4 == 0 and i % 100 != 0 or i % 400 == 0]


# uittest
class Test(unittest.TestCase):
    def test_square_nums(self):
        m = Mathematician()
        self.assertEqual(m.square_nums([1, 2]), [1, 4], 'Err')
        self.assertIsInstance(m.square_nums([1, 2]), list, 'Err')
        self.assertIsNotNone(m.square_nums([1, 2]), 'None')

    def test_remove_positives(self):
        m = Mathematician()
        self.assertEqual(m.remove_positives([26, -11, -8, 13, -90]), [-11, -8, -90], 'Err')
        self.assertIsInstance(m.remove_positives([26, -11, -8, 13, -90]), list, 'Err')
        self.assertIsNotNone(m.remove_positives([26, -11, -8, 13, -90]), 'None')

    def test_filter_leaps(self):
        m = Mathematician()
        self.assertEqual(m.filter_leaps([2001, 1884, 1995, 2003, 2020]), [1884, 2020], 'Err')
        self.assertIsInstance(m.filter_leaps([2001, 1884, 1995, 2003, 2020]), list, 'Err')
        self.assertIsNotNone(m.filter_leaps([2001, 1884, 1995, 2003, 2020]), 'None')


# pip install pytest
'''As for me: Очень удобная штука'''
# def plus(x):
#     return x+1
# def non():
#     pass
# def a_in_b():
#     a = 'a'
#     b = 'b'
#     return a + b
# def false_fun():
#     return False
# def test_plus():
#     assert plus(3) == 4
# def test_isinstance_plus():
#     assert isinstance(plus(3),int)
# def test_non():
#     assert non() == None
# def test_true_plus():
#     assert plus(3) == 4
# def test_false():
#     assert false_fun() == False
# def test_a_in_b():
#     assert 'a' in a_in_b()
# def test_is():
#     assert non() is None
if __name__ == '__main__':
    unittest.main()
