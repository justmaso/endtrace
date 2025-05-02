import unittest
from utils.validators import *

class TestValidators(unittest.TestCase):
    """Unit tests for coordinate and angle validation utilities."""

    def test_valid_coords(self):
        """Test that valid coordinates do not raise a CoordsError."""
        try:
            validate_coords(100, 200, 150, 250)
        except CoordsError:
            self.fail("validate_coords() raised CoordsError unexpectedly.")

    def test_invalid_coords_identical(self):
        """Test that identical coordinates raise a CoordsError."""
        with self.assertRaises(CoordsError):
            validate_coords(100, 200, 100, 200)

    def test_valid_angles(self):
        """Test that valid angles do not raise an AngleError."""
        try:
            validate_angles(45, 90)
        except AngleError:
            self.fail("validate_angles() raised AngleError unexpectedly.")

    def test_invalid_angles_identical(self):
        """Test that identical angles raise an AngleError."""
        with self.assertRaises(AngleError):
            validate_angles(60, 60)

    def test_invalid_angles_out_of_bounds_low(self):
        """
        Test that various angles below the valid Minecraft angle range of
        [-180, 180] raise an AngleError.
        """
        invalid_angle_pairs_below = [
            (-190, 30),
            (30, -190),
            (-200, -190),
            (-181, 0),
            (-181, -181)
        ]

        for angle1, angle2 in invalid_angle_pairs_below:
            with self.subTest(angle1=angle1, angle2=angle2):
                with self.assertRaises(AngleError):
                    validate_angles(angle1, angle2)

    def test_invalid_angles_out_of_bounds_high(self):
        """
        Test that various angles above the valid Minecraft angle range of
        [-180, 180] raise an AngleError.
        """
        invalid_angle_pairs_above = [
            (190, 0),
            (0, 190),
            (181, 100),
            (120, 181),
            (200, 300),
        ]

        for angle1, angle2 in invalid_angle_pairs_above:
            with self.subTest(angle1=angle1, angle2=angle2):
                with self.assertRaises(AngleError):
                    validate_angles(angle1, angle2)


if __name__ == "__main__":
    unittest.main()
