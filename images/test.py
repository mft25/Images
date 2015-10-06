from image_effects import *
import translations

filename = "test"
filename = "thames"
filename = "pumpkin"
filename = "me"

myImg = ImageEffects(filename, True)

#myImg.set_all_pixels([0xff, 0x88, 0x00, 0xff])
#myImg.pointillism(10, 3, 2) #(10, 0, 4)
#myImg.pixelate(15)
#myImg.blur(10)
#myImg.greyscale()
#myImg.colour_filter([0x00, 0xff, 0xff])
#myImg.translate(translations.waves(1000, 50))
myImg.greyscale().partition(50)


myImg.save(filename + myImg.effect)

myImg.open()