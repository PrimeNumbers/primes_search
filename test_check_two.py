import unittest
from check_two import check_two_

class TestCheckTwo(unittest.TestCase):

    def test_obvious(self):
        with self.assertRaises(ValueError):
            check_two_('0')
        with self.assertRaises(ValueError):
            check_two_('2')
        with self.assertRaises(ValueError):
            check_two_('4')
        with self.assertRaises(ValueError):
            check_two_('6')
        with self.assertRaises(ValueError):
            check_two_('8')

    def test_edge(self):
        self.assertFalse(check_two_('1'))
        self.assertFalse(check_two_('3'))
        self.assertFalse(check_two_('5'))
        self.assertFalse(check_two_('7'))
        self.assertFalse(check_two_('9'))


if __name__ == '__main__':
    unittest.main()
