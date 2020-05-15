photons = source.photon('100kVp, 2mm Al')
n = 256
scale = 0.1
angles = 128

phantom = ct_phantom(material.name, n, 1)

reconstructed = scan_and_reconstruct(photons, material, phantom, scale, angles, mas=10000, alpha=0.001)