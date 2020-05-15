import math
import numpy as np
import numpy.matlib
from scipy.fftpack import ifft, fft, fftfreq, fftshift, ifftshift

def ramp_filter(sinogram, scale, alpha=0.001):
	""" Ram-Lak filter with raised-cosine for CT reconstruction

	fs = ramp_filter(sinogram, scale) filters the input in sinogram (angles x samples)
	using a Ram-Lak filter.

	fs = ramp_filter(sinogram, scale, alpha) can be used to modify the Ram-Lak filter by a
	cosine raised to the power given by alpha."""

	# get input dimensions
	angles = sinogram.shape[0]
	n = sinogram.shape[1]

	#Set up filter to be at least twice as long as input
	m = np.ceil(np.log(2*n-1) / np.log(2))
	m = int(2 ** m)

	
	# the Ram Lak filter
	w_max = 2*np.pi / scale # scale since that's the 'width' of the X ray beam
	ramlak = np.abs(np.linspace(-w_max, w_max, m))
	

	"""

	# apply filter to all angles

	print('Ramp filtering')

	filtered = np.zeros((angles, n))
	for angle in range(angles):
		y = ifft(ramlak)
		filtered[angle] = np.convolve(y, sinogram[angle])

	"""
	filtered = np.zeros((angles, n))
	
	for angle in range(angles):

		signal = sinogram[angle]
		padding = int((m-n)/2)     # padding the signal
		signal = np.pad(signal, (padding, padding), constant_values = (0,0))

		f = fft(signal)
		f = fftshift(f)

		#freqs = fftfreq(len(f)) #* scale   # assuming scale is the sampling frequency?
		#freqs = fftshift(freqs)
		
		#f = np.multiply(f, np.abs(freqs))/(2*np.pi)

		#f = np.pad(f, (128, 128), constant_values = (0, 0))
		f = np.multiply(f, ramlak)

		f = ifftshift(f)
		f = ifft(f)

		filtered[angle] = f[padding:-padding]


	sinogram = filtered
	
	return sinogram