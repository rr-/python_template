"""Test the main routine."""
import argparse
from unittest.mock import patch

from template_project.__main__ import main


def test_main() -> None:
    """Test that the main routine does not raise an exception."""
    with patch(
        "template_project.__main__.parse_args",
        return_value=argparse.Namespace(),
    ):
        main()
