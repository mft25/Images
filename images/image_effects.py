import image
import random
		
class ImageEffects(image.Image):
	def for_all_pixels(self, function, *args, **kwargs):
		for j in xrange(0, self.h):
			for i in xrange(0, self.w):
				function(i, j, *args, **kwargs)
		
	def set_all_pixels(self, pixel):
		self.effect = "SetAllPixels"
		self.for_all_pixels(self.set_pixel, pixel)
		return self
		
	def greyscale(self):
		self.effect = "Greyscale"
		def _greyscale(i, j):
			pixel = self.get_pixel(i, j)
			ave = (pixel[0] + pixel[1] + pixel[2])/3
			self.set_pixel(i, j, [ave, ave, ave, 0xff])
		self.for_all_pixels(_greyscale)
		return self
		
	# colour should take format [0xrr, 0xgg, 0xbb]
	def colour_filter(self, colour):
		self.effect = "ColourFilter"
		def _colour_filter(i, j, colour):
			pixel = self.get_pixel(i, j)
			self.set_pixel(i, j, [(pixel[0]+colour[0])/2, (pixel[1]+colour[1])/2, (pixel[2]+colour[2])/2, 0xff])			
		self.for_all_pixels(_colour_filter, colour)
		return self
		
	def _pixelate(self, i, j, pixel_size, setter, *args, **kwargs):
		if j % pixel_size == 0 and i % pixel_size == 0:
			pixel_aggregate = [0, 0, 0, 0]
			count = 0
			for k in xrange(0, pixel_size**2):
				pixel = self.get_pixel(i + k%pixel_size, j + k/pixel_size)
				if pixel:
					pixel_aggregate = [sum(x) for x in zip(pixel_aggregate, pixel)]
					count = count + 1
			new_pixel = [pixel_aggregate[0]/count, pixel_aggregate[1]/count, pixel_aggregate[2]/count, 0xff]
			if kwargs and 'jitter' in kwargs:
				args = args + (random.randint(-kwargs['jitter'], kwargs['jitter']),)
				args = args + (random.randint(-kwargs['jitter'], kwargs['jitter']),)
			for k in xrange(0, pixel_size**2):
				setter(i + k%pixel_size, j + k/pixel_size, new_pixel, *args)

	def pixelate(self, pixel_size):
		self.effect = "Pixelate"
		def _standard_pixelator(i, j, pixel):
			self.set_pixel(i, j, pixel)
		self.for_all_pixels(self._pixelate, pixel_size, _standard_pixelator)
		return self

	def pointillism(self, radius, buffer=0, jitter=0):
		self.effect = "Pointillism"
		def _pointillism(i, j, pixel, radius, buffer, jitter_x, jitter_y):
			diameter = 2*radius
			if (radius - i%diameter)**2 + (radius - j%diameter)**2 < (radius-buffer)**2:
				self.set_pixel(i + jitter_x, j + jitter_y, pixel, True)
		self.new_canvas()
		self.for_all_pixels(self._pixelate, 2*radius, _pointillism, radius, buffer, jitter=jitter)
		self.img = self.canvas
		return self

	# This is very slow.
	def blur(self, reach):
		self.effect = "Blur"
		def _blur(i, j, reach):
			pixel_aggregate = [0, 0, 0, 0]
			count = 0
			for y in xrange(-reach, reach + 1):
				for x in xrange(-reach, reach + 1):
					pixel = self.get_pixel(i + x, j + y)
					if pixel:
						pixel_aggregate = [sum(x) for x in zip(pixel_aggregate, pixel)]
						count = count + 1
			new_pixel = [pixel_aggregate[0]/count, pixel_aggregate[1]/count, pixel_aggregate[2]/count, 0xff]
			self.set_pixel(i, j, new_pixel, True)
		self.new_canvas()
		self.for_all_pixels(_blur, reach)
		self.img = self.canvas
		return self
	
	def translate(self, function):
		self.effect = "Translate"
		def _translate(i, j, function):
			def _test(i, j):
				return (i, j)
			function = function if function else _test
			(x, y) = function(i, j)
			self.set_pixel(int(round(x)), int(round(y)), self.get_pixel(i, j), True)
		self.new_canvas()
		self.for_all_pixels(_translate, function)
		self.img = self.canvas
		return self
	
	def partition(self, range):
		self.effect = "Partition"
		def _partition(i, j, range):
			pixel = self.get_pixel(i, j)
			for k in xrange(0, 3):
				pixel[k] = min(range*(round(pixel[k]/float(range))), 0xff)
			self.set_pixel(i, j, pixel)
		self.for_all_pixels(_partition, range)
		return self
	