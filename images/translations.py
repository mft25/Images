import math

def waves(period, amplitude):
	def _waves(i, j):
		return (i + amplitude*math.sin((2*math.pi*j)/period), j)
	return _waves
	