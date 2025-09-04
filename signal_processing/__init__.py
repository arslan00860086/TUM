"""
Signal Processing Library for TUM

A basic signal processing library providing essential DSP functions.
"""

from .core import (
    generate_sine_wave,
    generate_noise,
    apply_low_pass_filter,
    apply_high_pass_filter,
    compute_fft,
    compute_ifft,
    analyze_signal
)

__version__ = "1.0.0"
__all__ = [
    "generate_sine_wave",
    "generate_noise", 
    "apply_low_pass_filter",
    "apply_high_pass_filter",
    "compute_fft",
    "compute_ifft",
    "analyze_signal"
]