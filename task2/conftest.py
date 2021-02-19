import pytest

from .calc import Calculator

@pytest.fixture(scope='class')
def init_cal():
    cal_obj = Calculator()
    return cal_obj