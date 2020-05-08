y1 = ct_detect(source.photon('100kVp, 2mm Al'), material.coeff('Water'), np.arange(0, 10.1, 0.1), 1)
plt.plot(np.log(y1), 'y') # this gives a straight line

y2 = ct_detect(source.photon('80kVp, 3mm Al'), material.coeff('Bone'), np.arange(0, 10.1, 0.1), 1)
plt.plot(np.log(y2), 'b') # this gives a straight line

plt.show()