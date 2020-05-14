photons = source.photon('100kVp, 2mm Al')
n = 256
scale = 0.1
angles = 90


phantom = ct_phantom(material.name, n, 6)

scan = ct_scan(photons, material, phantom, scale, angles)

sinogram = ct_calibrate(photons, material, scan, scale)

