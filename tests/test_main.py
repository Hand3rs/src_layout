import os

import main


def test_main_func():
    """Test a dumb function."""
    print(f"In test function: SOMEVAR: {os.getenv('SOMEVAR')}")
    assert main.main_func() == 314


def test_env_var():
    """Test value of env var."""
    print(f"In test function: SOMEVAR: {os.getenv('SOMEVAR')}")
    assert False
