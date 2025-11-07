import numpy as np
import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from ligotools.utils import whiten, write_wavfile, reqshift

def test_whiten_basic():
    dt = 1/4096
    t = np.linspace(0, 1, 4096)
    test_signal = np.sin(2*np.pi*100*t)

    # fake PSD (constant)
    interp_psd = lambda f: np.ones_like(f)

    white = whiten(test_signal, interp_psd, dt)

    assert len(white) == len(test_signal)
    assert not np.allclose(white, 0.0)

def test_reqshift_no_change_when_zero():
    sample_rate = 4096
    t = np.linspace(0, 1, sample_rate)
    test_signal = np.sin(2*np.pi*200*t)

    shifted_signal = reqshift(test_signal, fshift=0, sample_rate=sample_rate)

    assert np.allclose(shifted_signal, test_signal)