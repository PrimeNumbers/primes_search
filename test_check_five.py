import unittest
from check_five import check_five_

class TestCheckFive(unittest.TestCase):

    def test_obvious(self):
        y = 0
        while y <= 9:
            last_digit = str(y)[len(str(y))-1]
            #if there is no remainder after division
            if last_digit == '5':
                #it is divisible by ___ and should be rejected
                self.assertTrue(check_five_(last_digit))
            else:
                #otherwise it is not and should
                self.assertFalse(check_five_(last_digit))
            y+=1

if __name__ == '__main__':
    unittest.main()
