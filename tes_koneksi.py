import adi

sdr = adi.Pluto("ip:192.168.2.1")
print("Terhubung ke:", sdr.uri)
print("Sample rate :", sdr.sample_rate)