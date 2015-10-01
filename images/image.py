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
			
	def save(self, filename, use_canvas=False, includes_png=False):
		img = self.canvas if use_canvas else self.img
		self.out_filepath = self.out_image_dir + filename + ('' if includes_png else '.png')
		png.from_array(img, 'RGBA').save(self.out_filepath)
		
	def open(self):
		subprocess.call(('cygstart ' + self.out_filepath), shell=True)
	
	def display(self):
		if self.DEBUG:
			print self.img
			
	def new_canvas(self, pixel=[0xff, 0xff, 0xff, 0xff]):
		self.canvas = [[] for j in xrange(0, self.h)]
		for j in xrange(0, self.h):
			for i in xrange(0, self.w):
				self.canvas[j].extend(pixel)
			
	def get_pixel(self, i, j, use_canvas=False):
		img = self.canvas if use_canvas else self.img
		if i >= 0 and i < self.w and j >= 0 and j < self.h:
			return list(img[j][4*i:4*i+4])
		else:
			return None
		
	def set_pixel(self, i, j, pixel, use_canvas=False):
		img = self.canvas if use_canvas else self.img
		if i >= 0 and i < self.w and j >= 0 and j < self.h:
			for k in xrange(0,4):
				img[j][4*i + k] = pixel[k]
		