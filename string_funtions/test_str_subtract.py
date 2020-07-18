import unittest
from str_subtract import subtract

class TestSubtractStrings(unittest.TestCase):

    def test_obvious_small(self):
        self.assertEqual(subtract('100','50'), '50')
        self.assertEqual(subtract('9999','1234'), '8765')
        self.assertEqual(subtract('7','0'), '7')
        self.assertEqual(subtract('0','0'), '0')
        self.assertEqual(subtract('1234','0'), '1234')
        self.assertEqual(subtract('1002','3'), '999')
        self.assertEqual(subtract('5002','1000'), '4002')
        self.assertEqual(subtract('999','999'), '0')

    def test_edge(self):
        #negative should find it based length of b
        self.assertEqual(subtract('123','1234'), '-')
        #negative should find it based on the first digit
        self.assertEqual(subtract('123','456'), '-')
        #negative, but not discovered until part way through
        self.assertEqual(subtract('555535555','555545555'), '-')
        #large subtraction
        self.assertEqual(subtract('987654321987654321987654321','123456789123456789123456789'), '864197532864197532864197532')

if __name__ == '__main__':
    unittest.main()
