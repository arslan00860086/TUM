# TUM Signal Processing Library

A basic signal processing library providing essential digital signal processing (DSP) functions for educational and research purposes.

## Features

- **Signal Generation**: Create sine waves and various types of noise
- **Digital Filtering**: Apply low-pass and high-pass Butterworth filters
- **Frequency Analysis**: Fast Fourier Transform (FFT) and Inverse FFT
- **Signal Analysis**: Compute RMS, peak values, energy, and dominant frequencies

## Installation

1. Clone this repository:
```bash
git clone https://github.com/arslan00860086/TUM.git
cd TUM
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Signal Generation

```python
from signal_processing import generate_sine_wave, generate_noise

# Generate a 440 Hz sine wave for 1 second
time, signal = generate_sine_wave(frequency=440, duration=1.0, sample_rate=44100)

# Generate white noise
time, noise = generate_noise(duration=1.0, sample_rate=44100, noise_type='white')
```

### Filtering

```python
from signal_processing import apply_low_pass_filter, apply_high_pass_filter

# Apply a low-pass filter with 1000 Hz cutoff
filtered_signal = apply_low_pass_filter(signal, cutoff_freq=1000, sample_rate=44100)

# Apply a high-pass filter with 100 Hz cutoff
filtered_signal = apply_high_pass_filter(signal, cutoff_freq=100, sample_rate=44100)
```

### Frequency Analysis

```python
from signal_processing import compute_fft, analyze_signal

# Compute FFT
frequencies, magnitudes = compute_fft(signal, sample_rate=44100)

# Analyze signal properties
analysis = analyze_signal(signal, sample_rate=44100)
print(f"RMS: {analysis['rms']:.4f}")
print(f"Peak: {analysis['peak']:.4f}")
print(f"Dominant frequency: {analysis['dominant_frequency']:.1f} Hz")
```

## Demo

Run the demo script to see all features in action:

```bash
python demo.py
```

## Requirements

- Python 3.6+
- NumPy >= 1.20.0
- SciPy >= 1.7.0

## API Reference

### Signal Generation

- `generate_sine_wave(frequency, duration, sample_rate=44100, amplitude=1.0, phase=0.0)`
- `generate_noise(duration, sample_rate=44100, noise_type='white', amplitude=1.0)`

### Filtering

- `apply_low_pass_filter(signal_data, cutoff_freq, sample_rate, order=4)`
- `apply_high_pass_filter(signal_data, cutoff_freq, sample_rate, order=4)`

### Analysis

- `compute_fft(signal_data, sample_rate)`
- `compute_ifft(fft_data)`
- `analyze_signal(signal_data, sample_rate)`

## License

This project is open source and available under the MIT License.