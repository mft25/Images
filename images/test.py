from image_effects import *

filename = "test"
#filename = "thames"
#filename = "pumpkin"
filename = "me"

myImg = ImageEffects(filename, True)

#myImg.set_all_pixels([0xff, 0x88, 0x00, 0xff])
myImg.pointillism(10, 0, 4)
#myImg.pixelate(15)

myImg.save(filename + "Edited")


myImg.open()