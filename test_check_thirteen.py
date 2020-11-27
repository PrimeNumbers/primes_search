import unittest
from check_thirteen import check_thirteen_

class TestCheckThirteen(unittest.TestCase):

    def test_obvious(self):
        y = 0
        while y < 25000:
            #if there is no remainder after division
            if y % 13 == 0:
                #it is divisible by ___ and should be rejected
                self.assertTrue(check_thirteen_(str(y)))
            else:
                #otherwise it is not and should
                self.assertFalse(check_thirteen_(str(y)))
            y+=1

    def test_long(self):
        self.assertTrue(check_thirteen_('16049382583144577083971021'))
        self.assertTrue(check_thirteen_('215596063136887563'))
        self.assertFalse(check_thirteen_('123456789987654321'))
        self.assertFalse(check_thirteen_('1234567891011121314151617'))


if __name__ == '__main__':
    unittest.main()
