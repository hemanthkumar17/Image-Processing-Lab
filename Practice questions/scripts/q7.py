import numpy as np
import cv2

fft_basis = np.zeros((4, 4), dtype=complex)

for n in range(4):
  for k in range(4):
    fft_basis[n][k] = np.exp(-1j*2*np.pi*k*n/4)
print(fft_basis)