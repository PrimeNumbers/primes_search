import unittest
from check_seventeen import check_seventeen_

class TestCheckSeventeen(unittest.TestCase):

    def test_obvious(self):
        y = 0
        while y < 25000:
            #if there is no remainder after division
            if y % 17 == 0:
                #it is divisible by ___ and should be rejected
                self.assertTrue(check_seventeen_(str(y)))
            else:
                #otherwise it is not and should
                self.assertFalse(check_seventeen_(str(y)))
            y+=1

    def test_long(self):
        #divisible by ___
        self.assertTrue(check_seventeen_('3665133073327088571'))
        self.assertTrue(check_seventeen_('14295447902675205'))
        self.assertTrue(check_seventeen_('398144434437141421'))

        #not divisible by ___
        self.assertFalse(check_seventeen_('123456789987654321'))
        self.assertFalse(check_seventeen_('1234567891011121314151617'))
        self.assertFalse(check_seventeen_('16049382583144577083971021'))


if __name__ == '__main__':
    unittest.main()
