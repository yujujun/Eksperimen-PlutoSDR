import numpy as np
import matplotlib.pyplot as plt
import adi

# Koneksi ke PlutoSDR
sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = int(3e6)             
sdr.rx_lo = int(2.437e9)               
sdr.rx_rf_bandwidth = int(3e6)         
sdr.rx_buffer_size = 4096              
sdr.gain_control_mode_chan0 = "slow_attack"   

x = sdr.rx()                           
print("Jumlah sampel:", len(x), " tipe:", x.dtype)


sdr.rx_destroy_buffer()

X = np.fft.fftshift(np.fft.fft(x))
PSD = 10 * np.log10(np.abs(X)**2 / len(x) + 1e-12)

f = (np.fft.fftshift(np.fft.fftfreq(len(x), 1/sdr.sample_rate)) + sdr.rx_lo) / 1e6

plt.plot(f, PSD)
plt.xlabel("Frekuensi (MHz)")
plt.ylabel("Daya (dB)")
plt.title("Spektrum yang diterima Pluto")
plt.grid(True)
plt.tight_layout()
plt.show()