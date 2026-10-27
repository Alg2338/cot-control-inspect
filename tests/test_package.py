"""Basic checks for the initial package scaffold."""

import cot_control


def test_package_version() -> None:
    assert cot_control.__version__ == "0.1.0"
