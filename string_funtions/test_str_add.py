import unittest
from str_add import add

class TestAddingStrings(unittest.TestCase):

    def test_obvious_small(self):
        self.assertEqual(add('12345','54321'), '66666')
        self.assertEqual(add('123456','654321'), '777777')
        self.assertEqual(add('0','7'), '7')
        self.assertEqual(add('0','0'), '0')
        self.assertEqual(add('1234','0'), '1234')
        self.assertEqual(add('1002','3'), '1005')
        self.assertEqual(add('5002','1000'), '6002')
        self.assertEqual(add('999','999'), '1998')

    def test_edge(self):
        #large digit test
        self.assertEqual(add('99999999999999999999999999999','9999999999999999999999999999999999'), '10000099999999999999999999999999998')
        pass

if __name__ == '__main__':
    unittest.main()
