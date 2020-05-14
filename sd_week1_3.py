phantom = ct_phantom(material.name, 256, 6)

scan = ct_scan(source.photon('100kVp, 2mm Al'), material, phantom, 0.1, 90)

