import unittest
from unitasker import pressure_conversion, pascal_to_inches_of_mercury, imperial_fraction_to_mm, convert_fraction
class TestConversions(unittest.TestCase):
    def test_pressure_conversion_happy_path(self):
        self.assertAlmostEqual(pressure_conversion(1, 'bar', 'pascal'), 100000.0)
        self.assertAlmostEqual(pressure_conversion(1, 'atm', 'psi'), 14.6959, places=4)
    
    def test_invalid_unit(self):
        with self.assertRaises(ValueError):
            pressure_conversion(1, 'unknown_unit', 'psi')
    
    def test_pascal_to_inches_of_mercury(self):
        self.assertAlmostEqual(pascal_to_inches_of_mercury(101325), 29.9213, places=3)
    
    def test_fraction_to_mm(self):
        self.assertAlmostEqual(imperial_fraction_to_mm("1 1/2", "3/8")[0], 38.1)
        self.assertAlmostEqual(imperial_fraction_to_mm("1 1/2", "3/8")[1], 9.525)
    
    def test_invalid_fraction(self):
        with self.assertRaises(ValueError):
            convert_fraction("bad_input")

if __name__ == "__main__":
    unittest.main()