"""
Core signal processing functions

This module provides essential digital signal processing functions including
signal generation, filtering, FFT operations, and signal analysis.
"""

import numpy as np
from scipy import signal
from typing import Tuple, Optional


def generate_sine_wave(frequency: float, duration: float, sample_rate: int = 44100, 
                      amplitude: float = 1.0, phase: float = 0.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate a sine wave signal.
    
    Args:
        frequency: Frequency in Hz
        duration: Duration in seconds
        sample_rate: Sample rate in Hz (default: 44100)
        amplitude: Amplitude of the wave (default: 1.0)
        phase: Phase shift in radians (default: 0.0)
        
    Returns:
        Tuple of (time_array, signal_array)
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal_data = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    return t, signal_data


def generate_noise(duration: float, sample_rate: int = 44100, 
                  noise_type: str = 'white', amplitude: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate noise signal.
    
    Args:
        duration: Duration in seconds
        sample_rate: Sample rate in Hz (default: 44100)
        noise_type: Type of noise ('white', 'pink') (default: 'white')
        amplitude: Amplitude of the noise (default: 1.0)
        
    Returns:
        Tuple of (time_array, noise_array)
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    
    if noise_type == 'white':
        noise_data = amplitude * np.random.normal(0, 1, len(t))
    elif noise_type == 'pink':
        # Simple pink noise approximation
        white_noise = np.random.normal(0, 1, len(t))
        # Apply 1/f filter approximation
        freqs = np.fft.fftfreq(len(white_noise), 1/sample_rate)
        fft_white = np.fft.fft(white_noise)
        # Avoid division by zero
        freqs_safe = np.where(freqs == 0, 1e-10, freqs)
        pink_filter = 1 / np.sqrt(np.abs(freqs_safe))
        pink_filter[0] = 1  # DC component
        fft_pink = fft_white * pink_filter
        noise_data = amplitude * np.real(np.fft.ifft(fft_pink))
    else:
        raise ValueError("noise_type must be 'white' or 'pink'")
        
    return t, noise_data


def apply_low_pass_filter(signal_data: np.ndarray, cutoff_freq: float, 
                         sample_rate: int, order: int = 4) -> np.ndarray:
    """
    Apply a low-pass Butterworth filter to the signal.
    
    Args:
        signal_data: Input signal array
        cutoff_freq: Cutoff frequency in Hz
        sample_rate: Sample rate in Hz
        order: Filter order (default: 4)
        
    Returns:
        Filtered signal array
    """
    nyquist = sample_rate / 2
    normalized_cutoff = cutoff_freq / nyquist
    
    if normalized_cutoff >= 1:
        raise ValueError("Cutoff frequency must be less than Nyquist frequency")
        
    b, a = signal.butter(order, normalized_cutoff, btype='low')
    filtered_signal = signal.filtfilt(b, a, signal_data)
    return filtered_signal


def apply_high_pass_filter(signal_data: np.ndarray, cutoff_freq: float, 
                          sample_rate: int, order: int = 4) -> np.ndarray:
    """
    Apply a high-pass Butterworth filter to the signal.
    
    Args:
        signal_data: Input signal array
        cutoff_freq: Cutoff frequency in Hz
        sample_rate: Sample rate in Hz
        order: Filter order (default: 4)
        
    Returns:
        Filtered signal array
    """
    nyquist = sample_rate / 2
    normalized_cutoff = cutoff_freq / nyquist
    
    if normalized_cutoff >= 1:
        raise ValueError("Cutoff frequency must be less than Nyquist frequency")
        
    b, a = signal.butter(order, normalized_cutoff, btype='high')
    filtered_signal = signal.filtfilt(b, a, signal_data)
    return filtered_signal


def compute_fft(signal_data: np.ndarray, sample_rate: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute the Fast Fourier Transform of a signal.
    
    Args:
        signal_data: Input signal array
        sample_rate: Sample rate in Hz
        
    Returns:
        Tuple of (frequency_array, magnitude_array)
    """
    fft_result = np.fft.fft(signal_data)
    freqs = np.fft.fftfreq(len(signal_data), 1/sample_rate)
    
    # Return only positive frequencies
    positive_freq_idx = freqs >= 0
    freqs_positive = freqs[positive_freq_idx]
    magnitude = np.abs(fft_result[positive_freq_idx])
    
    return freqs_positive, magnitude


def compute_ifft(fft_data: np.ndarray) -> np.ndarray:
    """
    Compute the Inverse Fast Fourier Transform.
    
    Args:
        fft_data: FFT data array
        
    Returns:
        Time domain signal array
    """
    return np.real(np.fft.ifft(fft_data))


def analyze_signal(signal_data: np.ndarray, sample_rate: int) -> dict:
    """
    Analyze signal properties.
    
    Args:
        signal_data: Input signal array
        sample_rate: Sample rate in Hz
        
    Returns:
        Dictionary with signal analysis results
    """
    # Basic statistics
    rms = np.sqrt(np.mean(signal_data**2))
    peak = np.max(np.abs(signal_data))
    
    # Frequency domain analysis
    freqs, magnitude = compute_fft(signal_data, sample_rate)
    dominant_freq_idx = np.argmax(magnitude[1:]) + 1  # Skip DC component
    dominant_freq = freqs[dominant_freq_idx] if len(freqs) > 1 else 0
    
    # Signal energy
    energy = np.sum(signal_data**2)
    
    return {
        'rms': rms,
        'peak': peak,
        'crest_factor': peak / rms if rms > 0 else float('inf'),
        'energy': energy,
        'dominant_frequency': dominant_freq,
        'length': len(signal_data),
        'duration': len(signal_data) / sample_rate
    }