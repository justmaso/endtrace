import unittest
from utils.validators import *

class TestValidators(unittest.TestCase):
    def test_valid_coords(self):
        # should not raise
        try:
            validate_coords(100, 200, 150, 250)
        except CoordsError:
            self.fail("validate_coords() raised CoordsError unexpectedly")

    def test_invalid_coords_identical(self):
        with self.assertRaises(CoordsError):
            validate_coords(100, 200, 100, 200)

    def test_valid_angles(self):
        # should not raise
        try:
            validate_angles(45, 90)
        except AngleError:
            self.fail("validate_angles() raised AngleError unexpectedly")

    def test_invalid_angles_identical(self):
        with self.assertRaises(AngleError):
            validate_angles(60, 60)

    def test_invalid_angles_out_of_bounds_low(self):
        with self.assertRaises(AngleError):
            validate_angles(-190, 30)

    def test_invalid_angles_out_of_bounds_high(self):
        with self.assertRaises(AngleError):
            validate_angles(30, 200)

    def test_invalid_both_angles_out_of_bounds(self):
        with self.assertRaises(AngleError):
            validate_angles(-181, 181)


if __name__ == "__main__":
    unittest.main()
