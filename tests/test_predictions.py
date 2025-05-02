import unittest
import math
from unittest.mock import patch
from endtrace import _transform_minecraft_angle_to_cartesian_rads, predict_stronghold

def _normalize_angle_rad(theta: float) -> float:
    """
    Normalizes radian Cartesian angles to be from [0, 2pi).
    
    This is used to ensure consistent directional representation in
    tests. Although the endtrace algorithm can operate with any
    numerically equivalent angle (e.g., `-pi/4`, `7pi/4`, `-9pi/4`, etc.),
    tests require a consistent form to reliably compare expected and
    actual values.

    Args:
        theta (float): Angle in Cartesian radians.

    Returns:
        float: Normalized Cartesian radian angle in [0, 2pi).
    """
    return theta % (2*math.pi)


class TestPredictions(unittest.TestCase):
    """Tests for angle conversions and stronghold prediction output."""

    def _assert_angle_conversion(self, minecraft_degs, expected_rads):
        """
        Assert that Minecraft degree angles convert correctly to normalized
        Cartesian radians.

        Args:
            minecraft_degs (list[float]): Angles in Minecraft's angle system.
            expected_rads (list[float]): Expected normalized Cartesian radians.
        """
        for mc_deg, expected_rad in zip(minecraft_degs, expected_rads):
            ambig_rad = _transform_minecraft_angle_to_cartesian_rads(mc_deg)
            norm_rad = _normalize_angle_rad(ambig_rad)
            self.assertAlmostEqual(norm_rad, expected_rad)

    def test_transform_minecraft_angles_to_cartesian_rads_cardinals(self):
        """
        Test conversion of cardinal Minecraft angles to Cartesian radians.
        """
        minecraft_degrees = [180, -90, 0, 90]
        # cartesian_radians = [math.pi/2, 0, 3*math.pi/2, math.pi]
        cartesian_radians = [3*math.pi/2, 0, math.pi/2, math.pi]
        self._assert_angle_conversion(minecraft_degrees, cartesian_radians)
    
    def test_transform_minecraft_angles_to_cartesian_rads_non_cardinals(self):
        """
        Test conversion of non-cardinal Minecraft angles to Cartesian radians.
        """
        minecraft_degrees = [-135, -45, 45, 135]
        # cartesian_radians = [math.pi/4, 7*math.pi/4, 5*math.pi/4, 3*math.pi/4]
        cartesian_radians = [7*math.pi/4, math.pi/4, 3*math.pi/4, 5*math.pi/4]
        self._assert_angle_conversion(minecraft_degrees, cartesian_radians)

    def _get_printed_output(self, func, *args, **kwargs):
        """
        Helper to capture printed output from a function call.

        Args:
            func (callable): Function to call.
            *args: Positional arguments to pass to func.
            **kwargs: Keyword arguments to pass to func.
        
            Returns:
                str: Concatenated printed output.
        """
        with patch("builtins.print") as mock_print:
            func(*args, **kwargs)
            printed = "".join(
                str(arg)
                for call in mock_print.call_args_list
                for arg in call[0]
            )
            return printed

    def _assert_print_contains(self, printed, expected_strings):
        """
        Assert that printed output contains all expected substrings.

        Args:
            printed (str): Printed output text.
            expected_strings (list[str]): Substrings expected to be in printed.
        """
        for expected in expected_strings:
            self.assertIn(expected, printed)

    @patch("builtins.print")
    def test_predict_stronghold_prints_coords(self, mock_print):
        """Verify that predict_stronghold prints expected coordinate info."""
        theta1 = math.radians(-45)
        theta2 = math.radians(45)

        printed = self._get_printed_output(
            predict_stronghold,
            0, 0, theta1,
            0, 0, theta2
        )

        expected_strings = [
            "predicted stronghold coords",
            "(x=",
            "y=?",
            "z=",
            ")"
        ]

        self._assert_print_contains(printed, expected_strings)

    @patch("matplotlib.pyplot.show")
    @patch("builtins.print")
    def test_predict_stronghold_with_graph(self, mock_print, mock_show):
        """
        Test that predict_stronghold shows a graph when the --g/-g optional
        flag is used.
        """
        theta1 = math.radians(60)
        theta2 = math.radians(120)
        predict_stronghold(0, 0, theta1, 100, 0, theta2, graph=True)
        mock_show.assert_called_once()

    @patch("builtins.print")
    def test_predict_stronghold_origin_intersection(self, mock_print):
        """
        Test predict_stronghold outputs coordinates at the origin when we
        mathematically expect the intersection to be (0, 0)
        """
        printed = self._get_printed_output(
            predict_stronghold,
            10, -10, 45,
            -10, -10, -45
        )

        self.assertIn("x=0.0", printed)
        self.assertIn("z=0.0", printed)


if __name__ == "__main__":
    unittest.main()
