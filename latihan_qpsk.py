import numpy as np
import matplotlib.pyplot as plt

bits = np.random.randint(0, 2, (1000, 2))     
peta = {(0,0): 1+1j, (0,1): -1+1j, (1,1): -1-1j, (1,0): 1-1j}
sym = np.array([peta[tuple(b)] for b in bits]) / np.sqrt(2)

plt.figure(1)
plt.scatter(sym.real, sym.imag)
plt.title("Konstelasi QPSK (ideal)")
plt.xlabel("I (In-Phase)")
plt.ylabel("Q (Quadrature)")
plt.axis("equal"); plt.grid(True)

noise = 0.1 * (np.random.randn(len(sym)) + 1j*np.random.randn(len(sym)))
kotor = sym + noise

plt.figure(2)
plt.scatter(kotor.real, kotor.imag, s=5, color='orange')
plt.title("QPSK dengan derau saluran")
plt.xlabel("I (In-Phase)")
plt.ylabel("Q (Quadrature)")
plt.axis("equal"); plt.grid(True)

plt.show()