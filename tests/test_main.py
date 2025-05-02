import sys
import io
import unittest
from unittest.mock import patch
from contextlib import contextmanager
from endtrace import main

@contextmanager
def patched_main_env(args):
    """
    Context manager to patch builtins.print, sys.argv, and sys.stderr for
    running endtrace.main() in a controlled environment for testing.

    Args:
        args (list): List of command-line arguments to simulate.
    """
    with (
        patch("builtins.print"),
        patch.object(sys, "argv", ["endtrace"] + args),
        patch("sys.stderr", new_callable=io.StringIO)
    ): yield


class TestMainValidation(unittest.TestCase):
    """
    Tests for validating endtrace.main() argument parsing and error handling.
    """

    def _expect_exit(self, args, expected_code=1):
        """
        Helper method that runs endtrace.main() with given args expecting
        it to exit.

        Args:
            args (list): CLI arguments to simulate.
            expected_code (int): Expected SystemExit code.
        """
        with self.assertRaises(SystemExit) as cm:
            with patched_main_env(args):
                main()
    
        self.assertEqual(cm.exception.code, expected_code)

    def test_missing_theta2_exits(self):
        """Test main exits with error code 2 when theta2 arg is missing."""
        args = ["0", "0", "0", "0", "0"]
        self._expect_exit(args, expected_code=2)

    def test_identical_coords_exits(self):
        """Test main exits with error code 1 when coords are identical."""
        args = ["0", "0", "0", "0", "0", "0"]
        self._expect_exit(args)
    
    def test_parallel_throws_exits(self):
        """Test main exits with error code 1 when angles are parallel."""
        args = ["0", "0", "0", "10", "10", "0"]
        self._expect_exit(args)

    def test_valid_args_runs_successfully(self):
        """Test main runs without SystemExit on valid arguments."""
        args = ["0", "0", "-135", "100", "0", "135"]
        try:
            with patched_main_env(args):
                main()
        except SystemExit as e:
            self.fail(f"main() exited unexpectedly with code {e.code}")
    

if __name__ == "__main__":
    unittest.main()
