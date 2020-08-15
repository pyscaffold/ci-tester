import pytest

from ci_tester.skeleton import fib

__author__ = "Anderson Bravalheri"
__copyright__ = "Anderson Bravalheri"
__license__ = "MPL-2.0"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
