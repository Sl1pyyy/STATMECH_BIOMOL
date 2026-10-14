import math

R = 8.3145  # Universal gas constant in J/(mol*K)
T = 298.0  # Temperature in K

# Degeneracies
g_I = 2  # for 2-bromopropane (Isomer I)
g_II = 6  # for 1-bromopropane (Isomer II)

# Equilibrium mole fractions
x_I = 0.97  # Isomer I
x_II = 0.03  # Isomer II


# Problem 1

# Ratio N_II / N_I = (g_II / g_I) * exp(-Delta_E / (R * T)) = 3 / 97
# Delta_E = R * T * ln(97)
delta_E = R * T * math.log(97)  # J/mol
delta_E_kJ = delta_E / 1000  # kJ/mol
delta_E_kcal = delta_E / 4184  # kcal/mol

print(f"Energy difference (Delta E): {delta_E:.2f} J/mol")
print(f"Energy difference (Delta E): {delta_E_kJ:.2f} kJ/mol")
print(f"Energy difference (Delta E): {delta_E_kcal:.2f} kcal/mol\n")


# Problem 2

# Setting E_I = 0, then E_II = delta_E
E_I = 0.0
E_II = delta_E

# Mean energy of the mixture (Em = x_I*E_I + x_II*E_II)
mean_energy = (x_I * E_I) + (x_II * E_II)

# Partition function (q = g_I*exp(-E_I/RT) + g_II*exp(-E_II/RT))
q = (g_I * math.exp(-E_I / (R * T))) + (g_II * math.exp(-E_II / (R * T)))

# Molar free energy (G_m = -R * T * ln(q))
G_m = -R * T * math.log(q)
G_m_kJ = G_m / 1000

print(f"Mean energy (Em): {mean_energy:.2f} J/mol")
print(f"Partition function (q): {q:.4f}")
print(f"Free energy (Gm): {G_m:.2f} J/mol ({G_m_kJ:.2f} kJ/mol)")