import unittest
from str_divide import divide

class TestDivideStrings(unittest.TestCase):

    #cases to test
    # divide by 0 error
    # divide by 1
    # 0 divided by
    # 
    

    def test_obvious_small(self):
        self.assertEqual(divide('10','2'), '5')
        self.assertEqual(divide('2','3'), '0')
        self.assertEqual(divide('123','2'), '61')
        self.assertEqual(divide('2','123'), '0')
        self.assertEqual(divide('999','999'), '1')
        self.assertEqual(divide('2','99'), '0')
        self.assertEqual(divide('567','765'), '0')
        self.assertEqual(divide('500','100'), '5')
        self.assertEqual(divide('10000','1000'), '10')        
#        self.assertEqual(divide('',''), '')

    def test_edge(self):
        #should be if either is 0
        self.assertEqual(divide('0','123'), '0')
        self.assertEqual(divide('456','0'), '0')

        #negative should find it based on either being negative
        self.assertEqual(divide('-123','1234'), '-')
        self.assertEqual(divide('123','-456'), '-')
        #large divide
        self.assertEqual(divide('987654321987654321987654321','123456789123456789123456789'), '8')

if __name__ == '__main__':
    unittest.main()
