import unittest
from check_three import check_three_

class TestCheckThree(unittest.TestCase):

    def test_obvious(self):
        y = 0
        while y < 10000:
            #if there is no remainder after division
            if y % 3 == 0:
                #it is divisible by ___ and should be rejected
                self.assertTrue(check_three_(str(y)))
            else:
                #otherwise it is not and should
                self.assertFalse(check_three_(str(y)))
            y+=1

if __name__ == '__main__':
    unittest.main()
