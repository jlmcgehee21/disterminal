import pytest

from disterminal import helpers
import numpy as np

def main_call(x):
    out = np.zeros(x.shape)

    out[1] = 0.1
    out[-1] = 0.1

    return out

def test_autorange():
    x = helpers.autorange(main_call, '')

    assert x.shape == (100,)
    assert x.min() == pytest.approx(-9999.95)
    assert x.max() == pytest.approx(9999.95)
