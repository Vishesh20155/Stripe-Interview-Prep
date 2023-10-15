from calcs import Calculations
import unittest

class TestCalculations(unittest.TestCase):
    def test_get_sum(self):
        c = Calculations(3, 4)
        self.assertEquals(c.get_sum(), 7)
        
    def test_wrong_datatype(self):
        with self.assertRaises(TypeError):
            c = Calculations('3', 4)
        
if __name__ == '__main__':
    unittest.main()