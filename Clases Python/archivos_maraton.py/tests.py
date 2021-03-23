import unittest
from problemas import *

class TestProblemas(unittest.TestCase):
    def test_repeated_strings(self):
        self.assertEquals(repeated_string('aba', 10, 'a'), 7)
        self.assertEquals(repeated_string('abc', 10, 'd'), 0)
        self.assertEquals(repeated_string('abc', 10, 'a'), 4)
        self.assertEquals(repeated_string('abc', 10, 'b'), 3)

    def test_left_rotation(self):
        self.assertEquals(left_rotation([1,2,3,4,5,6], 1), [2,3,4,5,6,1])
        self.assertEquals(left_rotation([1,2,3,4,5,6], 2), [3,4,5,6,1,2])
        self.assertRaises(IndexError, left_rotation, [1], 2)
        self.assertEquals(left_rotation([1,2,3,4,5,6], 6), [1,2,3,4,5,6])

    def test_substring_share(self):
        self.assertCountEqual(substring_share('vaca', 'vacaciones'), ['v','a','c','va','ac','ca','vac','aca','vaca'])
        self.assertEquals(substring_share('e','e'), ['e'])
        self.assertEquals(substring_share('me', 'e'), ['e'])

    def test_anagrams(self):
        self.assertTrue(anagrams('a', 'a'))
        self.assertTrue(anagrams('genial', 'nigeal'))
        self.assertFalse(anagrams('a', 'b'))
        self.assertFalse(anagrams('genial', 'ggenial'))

    def test_binary(self):
        self.assertEquals(binary(1), "1")
        self.assertEquals(binary(2), "10")
        self.assertEquals(binary(4), "100")
        self.assertEquals(binary(10), "1010")
        self.assertEquals(binary(12), "1100")
        self.assertEquals(binary(18), "10010")
        self.assertEquals(binary(32), "100000")    

if __name__ == '__main__':
    unittest.main()