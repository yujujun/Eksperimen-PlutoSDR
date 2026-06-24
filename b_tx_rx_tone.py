import numpy as np
import adi
import matplotlib.pyplot as plt

sample_rate = int(3e6)     
center_freq = int(2.4e9)   
num_samps = 4096           

print("Menyambungkan ke PlutoSDR...")
sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = sample_rate

sdr.tx_lo = center_freq
sdr.tx_cyclic_buffer = True      
sdr.tx_hardwaregain_chan0 = -89  

sdr.rx_lo = center_freq
sdr.rx_rf_bandwidth = sample_rate
sdr.rx_buffer_size = num_samps
sdr.gain_control_mode_chan0 = 'manual'
sdr.rx_hardwaregain_chan0 = 0    

tone_freq = 100000 
t = np.arange(num_samps) / sample_rate

iq_samples = np.exp(1.0j * 2.0 * np.pi * tone_freq * t)

iq_samples = iq_samples * (2**14) 

print("Memancarkan sinyal Tone...")
sdr.tx(iq_samples)  

rx_data = sdr.rx()

sdr.tx_destroy_buffer()
print("Selesai.")
