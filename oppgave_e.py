import matplotlib.pyplot as plt
import numpy as np

k = 1.38e-23
Theta_R = 85.4
j = 50

T_theta = [1e-2, 1e-1, 1, 1e1, 1e2]

summa = 0
z = np.zeros(j+1)
for T in T_theta:
    for i in xrange(j+1):
        z[i] = (2*i + 1)*np.exp(-float(i*(i+1))*(T)**(-1))

    plt.plot(xrange(j+1), z)
plt.xlabel("j-values")
plt.ylabel("z(j)")
plt.title("Plot of z(j) for j $\epsilon$ [0, 50] for different $T/\\theta_r$-values")

plt.legend(["$T/\\theta_r = 1e-2$", "$T/\\theta_r = 1e-1$", "$T/\\theta_r = 1$", "$T/\\theta_r = 1e1$", "$T/\\theta_r = 1e2$"], loc = "upper right")
plt.show()
