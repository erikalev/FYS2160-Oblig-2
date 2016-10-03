import numpy as np
import matplotlib.pyplot as plt

### constants ###

k = 1.38e-23 # Bolzmann's constant

def calculate_Z(T):
    # the variable T is not T/theta_r
    j_max = 1000
    z_max = 1e-5
    Z = np.zeros(j_max)
    z = np.zeros(j_max)    
    Z[0] = 1
    j = 1
    Z_total = 0
    while j < j_max:
        z[j] = (2*j + 1)*np.exp(-j*(j + 1)*T**(-1))        
        Z[j] = Z[j-1] + z[j]
        if z[j]/max(z) < 0.001:
            Z_total = Z[j]
            break
        j += 1
    return Z_total
print calculate_Z(1)
