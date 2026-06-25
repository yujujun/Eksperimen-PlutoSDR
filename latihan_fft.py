import numpy as np
import matplotlib.pyplot as plt

N = 64
X = np.zeros(N, dtype=complex)
X[5] = 1                       # Taruh energi (data) di subcarrier ke-5
x = np.fft.ifft(X)             # Ubah ke domain waktu agar bisa dipancarkan antena

# Menggambar grafik
plt.subplot(2, 1, 1)
plt.plot(x.real)
plt.title("Domain Waktu (hasil IFFT)")

plt.subplot(2, 1, 2)
plt.plot(np.abs(np.fft.fft(x)))
plt.title("Domain Frekuensi (FFT lagi)")

plt.tight_layout()
plt.show()