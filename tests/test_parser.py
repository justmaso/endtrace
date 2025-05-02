import unittest
from unittest.mock import patch
import io
from utils.parser import parser

class TestParser(unittest.TestCase):
    """Unit tests for the command-line argument parser."""

    def test_parse_all_required_args(self):
        """
        Verify that all required positional arguments are parsed correctly
        as floats and that the graph flag (--g/-g) is False by default.
        """
        test_args = [
            "100",  # x1
            "200",  # z1
            "45",   # theta1
            "-100", # x2
            "-200", # z2
            "135"   # theta2
        ]
        parsed = parser.parse_args(test_args)
        self.assertEqual(parsed.x1, 100.0)
        self.assertEqual(parsed.z1, 200.0)
        self.assertEqual(parsed.theta1, 45.0)
        self.assertEqual(parsed.x2, -100.00)
        self.assertEqual(parsed.z2, -200.0)
        self.assertEqual(parsed.theta2, 135.0)
        self.assertFalse(parsed.graph)

    def test_parse_with_graph_flag(self):
        """
        Confirm that the --graph/-g optional flag is correctly parsed and set
        the graph attribute to True.
        """
        test_args = [
            "0", # x1
            "0", # z1
            "0", # theta1
            "0", # x2
            "0", # z2
            "0", # theta2
            "--graph"
        ]
        parsed = parser.parse_args(test_args)
        self.assertTrue(parsed.graph)

        test_args_short = [
            "0", # x1
            "0", # z1
            "0", # theta1
            "0", # x2
            "0", # z2
            "0", # theta2
            "-g"
        ]
        parsed_short = parser.parse_args(test_args_short)
        self.assertTrue(parsed_short.graph)

    @patch("sys.stderr", new_callable=io.StringIO)
    def test_missing_required_args(self, _):
        """
        Test that missing positional arguments cause the parser ot exit with
        a SystemExit exception.
        """
        incomplete_args = [
            "0", # x1
            "0", # z1
            "0", # theta1
            "0", # x2
            "0", # z2
            # missing theta2
        ]
        with self.assertRaises(SystemExit):
            parser.parse_args(incomplete_args)


if __name__ == "__main__":
    unittest.main()
