phantom = ct_phantom(material.name, 256, 2)

scan = ct_scan(source.photon('100kVp, 2mm Al'), material, phantom, 0.1, 60)
# something about positional argument cannot follow keyword argument
