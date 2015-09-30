import Image
		
class ImageEffects(Image.Image):
	def for_all_pixels(self, function, *args):
		for j in xrange(0, self.h):
			for i in xrange(0, self.w):
				function(i, j, *args)
		
	def set_all_pixels(self, pixel):
		self.for_all_pixels(self.set_pixel, pixel)
		
	def _pixelate(self, i, j, pixel_size, setter, *args):
		if j % pixel_size == 0 and i % pixel_size == 0:
			pixel_aggregate = [0, 0, 0, 0x0]
			count = 0
			for k in xrange(0, pixel_size**2):
				if (i + k%pixel_size) < self.w and (j + k/pixel_size) < self.h:
					pixel = self.get_pixel(i + k%pixel_size, j + k/pixel_size)
					pixel_aggregate = [sum(x) for x in zip(pixel_aggregate, pixel)]
					count = count + 1
			new_pixel = [pixel_aggregate[0]/count, pixel_aggregate[1]/count, pixel_aggregate[2]/count, 0xff]
			for k in xrange(0, pixel_size**2):
				if (i + k%pixel_size) < self.w and (j + k/pixel_size) < self.h:
					setter(i + k%pixel_size, j + k/pixel_size, new_pixel, *args)

	def pixelate(self, pixel_size):
		def _standard_pixelator(i, j, pixel):
			self.set_pixel(i, j, pixel)
		self.for_all_pixels(self._pixelate, pixel_size, _standard_pixelator)

	def pointillism(self, radius, buffer):
		def _pointillism(i, j, pixel, radius, buffer):
			diameter = 2*radius
			if (radius - i%diameter)**2 + (radius - j%diameter)**2 < (radius-buffer)**2:
				self.set_pixel(i, j, pixel)
			else:
				self.set_pixel(i, j, [0xff, 0xff, 0xff, 0xff])
		self.for_all_pixels(self._pixelate, 2*radius, _pointillism, radius, buffer)

