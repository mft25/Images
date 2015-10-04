from image_effects import *

filename = "test"
filename = "thames"
filename = "pumpkin"
#filename = "me"

myImg = ImageEffects(filename, True)

#myImg.set_all_pixels([0xff, 0x88, 0x00, 0xff])
#myImg.pointillism(10, 3, 2)
#myImg.pixelate(15)
myImg.blur(2)

myImg.save(filename + "Edited")


myImg.open()