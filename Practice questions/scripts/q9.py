import numpy as np
import cv2

def fft(u, v):
    fft_basis = np.zeros([4, 4], dtype=complex)
    for x in range(4):
        for y in range(4):
            fft_basis[x, y] = np.exp(-1j*2*np.pi*(u*x + v*y)/4)
    return fft_basis
    
F = fft(1, 1) * 3 + fft(1, 2) * 2
print(F)

# [[ 5  -5j -5 +5j]
#  [-2-3j -3+2j 2+3j  3-2j]
#  [-1  +1j 1+0j  -1j]
#  [-2+3j  3+2j 2-3j -3-2j]]

# The hard way
#
# f = np.zeros((4, 4))
# F = np.zeros((4, 4), dtype=complex)
# f[1, 1] = 3
# f[1, 2] = 2

# for x in range(4):
#   for y in range(4):
#       for u in range(4):
#           for v in range(4):
#             F[x, y] = F[x, y] + f[u, v] * np.exp(-1j*2*np.pi*(u*x + v*y)/4)
# print(F)

F = np.abs(F)
cv2.imshow("image", F)
