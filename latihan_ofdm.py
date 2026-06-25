import numpy as np

N = 64       
CP = 16      

bits = np.random.randint(0, 2, (N, 2))
peta = {(0,0): 1+1j, (0,1): -1+1j, (1,1): -1-1j, (1,0): 1-1j}
X = np.array([peta[tuple(b)] for b in bits]) / np.sqrt(2)

x = np.fft.ifft(X)

x_cp = np.concatenate([x[-CP:], x])
print("Panjang tanpa CP:", len(x), " dengan CP:", len(x_cp))

y = x_cp[CP:]
X_terima = np.fft.fft(y)
print("Selisih maksimum dengan data asli:", np.max(np.abs(X_terima - X)))