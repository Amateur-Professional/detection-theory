"""Basic signal metrics."""

import numpy as np


def rms(x):
    """Root-mean-square amplitude of a signal."""
    x = np.asarray(x, dtype=float)
    if x.size == 0:
        raise ValueError("rms is undefined for an empty signal")
    return float(np.sqrt(np.mean(x**2)))


def to_db(power, reference=1.0):
    """Convert a power ratio to decibels.

    Raises on non-positive input rather than returning -inf, so that a
    silent zero upstream surfaces here instead of propagating.
    """
    power = np.asarray(power, dtype=float)
    if np.any(power <= 0):
        raise ValueError("power must be strictly positive")
    return 10.0 * np.log10(power / reference)

def _scratch( x ):
    y=1
