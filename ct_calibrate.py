import numpy as np
import scipy
from scipy import interpolate
import math
from ct_detect import ct_detect

def ct_calibrate(photons, material, sinogram, scale, correct=True):

	""" ct_calibrate convert CT detections to linearised attenuation
	sinogram = ct_calibrate(photons, material, sinogram, scale) takes the CT detection sinogram
	in x (angles x samples) and returns a linear attenuation sinogram
	(angles x samples). photons is the source energy distribution, material is the
	material structure containing names, linear attenuation coefficients and
	energies in mev, and scale is the size of each pixel in x, in cm."""

	# ct_calibrate(source.photon('100kVp, 2mm Al'), material, scan, 0.1

	# Get dimensions and work out detection for just air of twice the side
	# length (has to be the same as in ct_scan.py)
	n = sinogram.shape[1]
	angles = sinogram.shape[0]

	#depth[air] = 2 * n - np.sum(depth, axis=0)

	depth_air = np.zeros(sinogram.shape)
	values = np.zeros((sinogram.shape))
	dummy = np.ones((n, n))

	for angle in range(angles):

		# get input image dimensions, and create a coordinate structure
		xi, yi = np.meshgrid(np.arange(n) - (n/2) + 0.5, np.arange(n) - (n/2) + 0.5)

		# Get rotated coordinates for interpolation
		p = -math.pi / 2 - angle * math.pi / angles
		x0 = xi * math.cos(p) - yi * math.sin(p) + (n/2) - 0.5
		y0 = xi * math.sin(p) + yi * math.cos(p) + (n/2) - 0.5

		interpolated = scipy.ndimage.map_coordinates(dummy, [y0, x0], order=1, mode='constant', cval=0, prefilter=False)

		depth = np.sum(interpolated, axis = 0)

		depth_air[angle] = 2*n - depth
		#depth_air[angle] = depth

	for angle in range(angles):
		for i in range(n):
			values[angle][i] = ct_detect(photons, material.coeff('Air'), depth_air[angle][i])
			#values = attenuate(photons, coeff, depth[angle][i])

	
	sinogram_att = -np.log( np.divide(sinogram, values) )
	sinogram = sinogram_att

	# perform calibration

	return sinogram