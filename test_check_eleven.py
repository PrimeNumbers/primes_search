import unittest
from check_eleven import check_eleven_

class TestCheckEleven(unittest.TestCase):

    def test_obvious(self):
        y = 0
        divisor = 11
        while y < 25000:
            #if there is no remainder after division
            if y % divisor == 0:
                #it is divisible by ___ and should be rejected
                self.assertTrue(check_eleven_(str(y)))
            else:
                #otherwise it should not be eliminated, (aka remain a candidate)
                self.assertFalse(check_eleven_(str(y)))
            y+=1

    def test_long(self):
        self.assertFalse(check_eleven_('123456789100987654321'))
        self.assertFalse(check_eleven_('1234567891234567899'))
        self.assertTrue(check_eleven_('135802468010'))
        self.assertTrue(check_eleven_('1358024680358024679'))
        

if __name__ == '__main__':
    unittest.main()
