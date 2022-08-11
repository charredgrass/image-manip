from PIL import Image

#Objective:
# Place image on screen and rapidly flip it so it appears 
#   to be slashing a target.
# Concatenate the second gif to the end of the image.
#

output = []


with Image.open("georgesuo.png") as img:
	for x in range(5):
		#
		delay = x*20









output[0].save('diesofgeorge.gif', save_all=True, append_images=output[1:], loop=0, disposal=2)