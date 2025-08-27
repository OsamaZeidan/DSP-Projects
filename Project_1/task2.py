import numpy as np
import matplotlib.pyplot as plt

fs = 100  # Sampling frequency (Hz)
t = np.arange(0, 1, 1/fs)
# Signal frequencies
f1 = 1  # Frequency of S1 (1 Hz)
f2 = 4  # Frequency of S2 (4 Hz)
f3 = 10 # Frequency of S3 (10 Hz)
S1 = np.cos(2 * np.pi * f1 * t)
S2 = np.cos(2 * np.pi * f2 * t)
S3 = np.cos(2 * np.pi * f3 * t)
X = 2 * S1 + 4 * S2 + S3
Y = S1 + S2
plt.figure(figsize=(12, 10))
plt.subplot(4, 1, 1)
plt.plot(t, S1, label='S1 (1 Hz)')
plt.title('Signal S1 (1 Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(t, S2, label='S2 (4 Hz)', color='orange')
plt.title('Signal S2 (4 Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(t, S3, label='S3 (10 Hz)', color='green')
plt.title('Signal S3 (10 Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(t, X, label='X = 2S1 + 4S2 + S3', color='purple')
plt.plot(t, Y, label='Y = S1 + S2', color='red', linestyle='--')
plt.title('Signals X and Y')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.tight_layout()
plt.show()
# Standard correlation of S1 with X and Y
standard_correlation_X = np.sum(S1 * X)
standard_correlation_Y = np.sum(S1 * Y)
# Normalized correlation of S1 with X and Y
normalized_correlation_X = np.sum(S1 * X) / (np.sqrt(np.sum(S1**2)) * np.sqrt(np.sum(X**2)))
normalized_correlation_Y = np.sum(S1 * Y) / (np.sqrt(np.sum(S1**2)) * np.sqrt(np.sum(Y**2)))
print(f"Standard correlation of S1 in X: {standard_correlation_X}")
print(f"Standard correlation of S1 in Y: {standard_correlation_Y}")
print(f"Normalized correlation of S1 in X: {normalized_correlation_X}")
print(f"Normalized correlation of S1 in Y: {normalized_correlation_Y}")
