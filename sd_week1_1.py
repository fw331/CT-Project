from material import Material
import matplotlib.pyplot as plt
import numpy as np

m = Material()
# note: m.mev is the energies (in MeV) for which attenuation values for different materials is available

#print(len(m.mev))
#print(len(m.coeff('Blood')))

compton = np.reciprocal(m.mev)
photo = np.reciprocal((np.power(m.mev, 3)))

plt.plot(m.mev, m.coeff('Blood'))
plt.plot(m.mev, compton, 'y')
plt.plot(m.mev, photo, 'r')
plt.legend(['Blood', 'Compton', 'Photoelectric'])
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Energy')
plt.ylabel('Attenuation')
plt.show()