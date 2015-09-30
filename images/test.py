from image_effects import *

filename = "me"
filename = "test"
filename = "thames"
filename = "pumpkin"

myImg = ImageEffects(filename, True)

#myImg.set_all_pixels([0xff, 0x88, 0x00, 0xff])
myImg.pointillism(20, 2)

myImg.save(filename + "Edited")


myImg.open()