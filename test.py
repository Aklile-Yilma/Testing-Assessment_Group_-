import unittest
from string_functions import *

class TestToUpper(unittest.TestCase):
    # write your code here
    def testToUpper(self):
        test_string = "cat"
        self.assertEqual(test_string.upper(), to_upper(test_string))
        
        test_string = 1
        with self.assertRaises(TypeError):
            to_upper(test_string)
            
    
class TestToLower(unittest.TestCase):
    # Write you code here
    def testToLower(self):
        test_string = "cat"
        self.assertEqual(test_string.lower(), to_lower(test_string))
        
        test_string = 1
        with self.assertRaises(TypeError):
            to_lower(test_string)
    
class TestCapitalize(unittest.TestCase):
    # Write your code here
    def testCapitalize(self):
        test_string = "cat"
        self.assertEqual(test_string.capitalize(), capitalize(test_string))
        
        test_string = 1
        with self.assertRaises(TypeError):
            to_lower(test_string)
    

if __name__ == '__main__':
    unittest.main()
