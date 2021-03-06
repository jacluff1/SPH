import numpy as np

def heaviside(x,shift=0):
    return 0.5 * (np.sign(x-shift) + 1)

def direction(vec):
    return vec/np.linalg.norm(vec)
