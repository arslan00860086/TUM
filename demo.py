#!/usr/bin/env python3
"""
Signal Processing Demo

This script demonstrates the basic functionality of the signal processing library.
"""

import numpy as np
from signal_processing import (
    generate_sine_wave,
    generate_noise,
    apply_low_pass_filter,
    compute_fft,
    analyze_signal
)


def demo_signal_generation():
    """Demonstrate signal generation capabilities."""
    print("=== Signal Generation Demo ===")
    
    # Generate a sine wave
    t, sine_wave = generate_sine_wave(frequency=440, duration=1.0, sample_rate=8000)
    print(f"Generated sine wave: {len(sine_wave)} samples, {sine_wave.dtype}")
    
    # Generate noise
    t_noise, noise = generate_noise(duration=1.0, sample_rate=8000, noise_type='white')
    print(f"Generated white noise: {len(noise)} samples")
    
    # Combine sine wave with noise
    noisy_signal = sine_wave + 0.1 * noise
    print(f"Created noisy signal")
    
    return t, sine_wave, noisy_signal


def demo_filtering():
    """Demonstrate filtering capabilities."""
    print("\n=== Filtering Demo ===")
    
    # Create a test signal with multiple frequencies
    sample_rate = 8000
    t = np.linspace(0, 1, sample_rate, endpoint=False)
    
    # Combine multiple sine waves
    signal_data = (np.sin(2 * np.pi * 100 * t) +  # 100 Hz
                   0.5 * np.sin(2 * np.pi * 500 * t) +  # 500 Hz
                   0.3 * np.sin(2 * np.pi * 1500 * t))  # 1500 Hz
    
    # Apply low-pass filter
    filtered_signal = apply_low_pass_filter(signal_data, cutoff_freq=800, sample_rate=sample_rate)
    print(f"Applied low-pass filter with cutoff at 800 Hz")
    
    return t, signal_data, filtered_signal


def demo_fft_analysis():
    """Demonstrate FFT analysis."""
    print("\n=== FFT Analysis Demo ===")
    
    # Generate a test signal
    sample_rate = 8000
    t, test_signal = generate_sine_wave(frequency=440, duration=0.5, sample_rate=sample_rate)
    
    # Add some noise
    _, noise = generate_noise(duration=0.5, sample_rate=sample_rate)
    noisy_signal = test_signal + 0.1 * noise
    
    # Compute FFT
    freqs, magnitude = compute_fft(noisy_signal, sample_rate)
    
    # Find dominant frequency
    dominant_idx = np.argmax(magnitude[1:]) + 1  # Skip DC
    dominant_freq = freqs[dominant_idx]
    
    print(f"Original frequency: 440 Hz")
    print(f"Detected dominant frequency: {dominant_freq:.1f} Hz")
    
    return freqs, magnitude


def demo_signal_analysis():
    """Demonstrate signal analysis."""
    print("\n=== Signal Analysis Demo ===")
    
    # Generate test signals
    sample_rate = 8000
    t, clean_signal = generate_sine_wave(frequency=1000, duration=0.5, sample_rate=sample_rate)
    t, noise = generate_noise(duration=0.5, sample_rate=sample_rate)
    
    # Analyze clean signal
    clean_analysis = analyze_signal(clean_signal, sample_rate)
    print("Clean sine wave analysis:")
    for key, value in clean_analysis.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.4f}")
        else:
            print(f"  {key}: {value}")
    
    # Analyze noise
    noise_analysis = analyze_signal(noise, sample_rate)
    print("\nNoise analysis:")
    for key, value in noise_analysis.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.4f}")
        else:
            print(f"  {key}: {value}")


def main():
    """Run all demonstrations."""
    print("Signal Processing Library Demo")
    print("=" * 40)
    
    try:
        # Run demos
        demo_signal_generation()
        demo_filtering()
        demo_fft_analysis()
        demo_signal_analysis()
        
        print("\n=== Demo completed successfully! ===")
        
    except Exception as e:
        print(f"Error during demo: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()