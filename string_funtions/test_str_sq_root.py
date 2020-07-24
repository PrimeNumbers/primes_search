import unittest
from str_sq_root import sq_root

class TestSqRootStrings(unittest.TestCase):

    #only strings that are positive and only contain string.digits can be considered
    #it is designed to find the int(square_root) for numbers that are very long.

    def test_obvious_small(self):
        self.assertEqual(sq_root('9876543210'), '99380')
        self.assertEqual(sq_root('98765432100'), '314269')
        self.assertEqual(sq_root('98765'), '314')
        self.assertEqual(sq_root('1000'), '31')
        self.assertEqual(sq_root('12345'), '111')
        self.assertEqual(sq_root('123456'), '351')
        self.assertEqual(sq_root('7654321'), '2766')
        self.assertEqual(sq_root('985019836409176391872698'), '992481655452')

    def test_edge(self):
        #unconfirmed long numbers
        #mostly as a log of where the program was at
        self.assertEqual(sq_root('98501983640917639187269810234987109238471093285610975610934610934871029384710938461093284619328461023984709'), '313850256716348153423387893177135769962871663087579665')


if __name__ == '__main__':
    unittest.main()
