import unittest
from check_seven import check_seven_

class TestCheckSeven(unittest.TestCase):

    def test_obvious(self):
        y = 0
        while y < 10000:
            #if there is no remainder after division
            if y % 7 == 0:
                #it is divisible by ___ and should be rejected
                self.assertTrue(check_seven_(str(y)))
            else:
                #otherwise it is not and should
                self.assertFalse(check_seven_(str(y)))
            y+=1

if __name__ == '__main__':
    unittest.main()
