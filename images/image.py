import png
import subprocess

class Image(object):
	DEBUG = False
	
	def __init__(self, filename, read=False, includes_png=False):
		self.src_image_dir = 'SourceImages/'
		self.out_image_dir = 'OutImages/'
		self.src_filepath = self.src_image_dir + filename + ('' if includes_png else '.png')
		if read:
			self.read()

	def read(self):
		r = png.Reader(self.src_filepath)
		img_src = r.asRGBA()
		self.img = [list(item) for item in list(img_src[2])]
		self.h = len(self.img)
		self.w = len(self.img[0])/4
			
	def save(self, filename, includes_png=False):
		self.out_filepath = self.out_image_dir + filename + ('' if includes_png else '.png')
		png.from_array(self.img, 'RGBA').save(self.out_filepath)
		
	def open(self):
		subprocess.call(('cygstart ' + self.out_filepath), shell=True)
	
	def display(self):
		if self.DEBUG:
			print self.img
			
	def get_pixel(self, i, j):
		return list(self.img[j][4*i:4*i+4])
		
	def set_pixel(self, i, j, pixel):
		for k in xrange(0,4):
			self.img[j][4*i + k] = pixel[k]
		