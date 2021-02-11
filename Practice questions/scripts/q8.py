import numpy as np
import cv2

fft_basis = np.zeros([4, 4, 4, 4], dtype=complex)

for u in range(4):
  for v in range(4):
      for x in range(4):
          for y in range(4):
            fft_basis[u, v, x, y] = np.exp(-1j*2*np.pi*(u*x + v*y)/4)
print("Direct")
print(fft_basis)

fft1_basis = np.zeros((4, 4), dtype=complex)
fft2_basis = np.zeros([4, 4, 4, 4], dtype=complex)
for u in range(4):
    for x in range(4):
        fft1_basis[u, x] = np.exp(-1j*2*np.pi*u*x/4)
for x in range(4):
    for y in range(4):
        for u in range(4):
            for v in range(4):
                fft2_basis[x, y, u, v] = fft1_basis[u, x] * fft1_basis[v, y]
print("From 1D")
print(fft2_basis)