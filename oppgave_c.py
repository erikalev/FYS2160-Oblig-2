import matplotlib.pyplot as plt
import numpy as np
N = 15000
eV = 1.602e-19
k = 1.38e-23
e = -1.5*eV
T = np.linspace(1, N, N)
Cv = 3*e**2/(k*T**2)*np.exp(e/(k*T))/((np.exp(e/(k*T)) + 3)**2)
plt.plot(T, Cv, "-r")
plt.xlabel("Temperatur [K]")
plt.xscale("log")
plt.ylabel("Heat Capacity [J/K]")
plt.title("Assignment 1c, Oblig 2")
plt.show()
