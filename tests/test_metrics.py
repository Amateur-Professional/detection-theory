import numpy as np
import pytest

from detection_theory.metrics import rms, to_db


def test_rms_of_unit_sine_is_one_over_sqrt_two():
    t = np.linspace(0, 1, 10_000, endpoint=False)
    assert rms(np.sin(2 * np.pi * 5 * t)) == pytest.approx(1 / np.sqrt(2), abs=1e-3)


def test_rms_of_dc_equals_magnitude():
    assert rms(np.full(100, 3.0)) == pytest.approx(3.0)


def test_rms_rejects_empty():
    with pytest.raises(ValueError):
        rms([])


@pytest.mark.parametrize("power, expected", [(1.0, 0.0), (10.0, 10.0), (0.5, -3.0103)])
def test_to_db_known_values(power, expected):
    assert to_db(power) == pytest.approx(expected, abs=1e-3)


def test_to_db_rejects_non_positive():
    with pytest.raises(ValueError):
        to_db(0.0)
