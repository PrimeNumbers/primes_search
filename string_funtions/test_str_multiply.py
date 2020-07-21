import unittest
from str_multiply import multiply

class TestMultiplyStrings(unittest.TestCase):

    def test_obvious_small(self):
        self.assertEqual(multiply('1','1'), '1')
        self.assertEqual(multiply('2','3'), '6')
        self.assertEqual(multiply('123','2'), '246')
        self.assertEqual(multiply('2','123'), '246')
        self.assertEqual(multiply('999','999'), '998001')
        self.assertEqual(multiply('2','99'), '198')
        self.assertEqual(multiply('567','765'), '433755')
#        self.assertEqual(multiply('',''), '')

    def test_edge(self):
        #should be if either is 0
        self.assertEqual(multiply('0','123'), '0')
        self.assertEqual(multiply('456','0'), '0')
        #negative should find it based on either being negative
        self.assertEqual(multiply('-123','1234'), '-')
        self.assertEqual(multiply('123','-456'), '-')
        #large multiplication
        self.assertEqual(multiply('987654321987654321987654321','123456789123456789123456789'), '121932631356500531591068431581771069347203169112635269')

if __name__ == '__main__':
    unittest.main()
