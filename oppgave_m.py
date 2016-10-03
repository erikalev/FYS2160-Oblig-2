import matplotlib.pyplot as plt
import numpy as np

#k = 1.0 #1.38e-23 # Bolzmann's constant

"""
T is the value of theta_r / T
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

T = np.linspace(1e-2, 10, N) # T is now T/theta_r

Z = np.zeros(N)
for i in xrange(N):
    Z[i] = calculate_Z(T[i])

B = 1.0/T # setting k = 1.0

E = -np.diff(np.log(Z))/np.diff(B)
Cv = np.diff(E)/np.diff(T[0:N-1])

plt.plot(T[0:N-2], Cv)
plt.xlabel("T/theta")
plt.ylabel("Cv")
plt.title("Normalized heat capasity Cv(T/$\\theta_r$)")
plt.show()
plt.plot(T[0:N-1], E)
plt.legend(["Cv", "E"])
plt.xlabel("T/theta")
plt.ylabel("E(T/$\\theta_r$)")
plt.title("Normalized energy E(T/$\\theta_r$)")
plt.show()
