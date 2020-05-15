import numpy as np
import scipy
from scipy import interpolate
from ct_phantom import *
from ct_scan import *

def ct_calibrate(photons, material, sinogram, scale, correct=True):

	""" ct_calibrate convert CT detections to linearised attenuation
	sinogram = ct_calibrate(photons, material, sinogram, scale) takes the CT detection sinogram
	in x (angles x samples) and returns a linear attenuation sinogram
	(angles x samples). photons is the source energy distribution, material is the
	material structure containing names, linear attenuation coefficients and
	energies in mev, and scale is the size of each pixel in x, in cm."""

	# Get dimensions and work out detection for just air of twice the side
	# length (has to be the same as in ct_scan.py)

	n = sinogram.shape[1]
	angles = sinogram.shape[0]

	phantom_air = d = ct_phantom(material.name, n, 9) #added type, with the single point attenuator of tissue replaced with air

	sinogram_air = ct_scan(photons, material, phantom_air, scale, angles)

	sinogram = -np.log( np.divide(sinogram, sinogram_air))

	# perform calibration

	return sinogram
