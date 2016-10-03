import numpy as np
import matplotlib.pyplot as plt

"""
T is the value T/theta_r
"""

def calculate_Z(T):
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
N = 500
T = np.linspace(1e-2, 10, N)
Z = np.zeros(N)
Z[0] = 1
for i in xrange(1, N):
    Z[i] = calculate_Z(T[i])
plt.plot(T, Z)
plt.xlabel("T/$\\theta_r$")
plt.ylabel("Z(T/$\\theta_r$)")
plt.title("Plot of Z(T/$\\theta_r$)")
plt.show()
