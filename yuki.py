from PIL import Image

# im = Image.open("snow.gif")

output = []

with Image.open("snow.gif") as img:

	# img.seek(0)
	for x in range(4):
		theta = -90 * x
		img.seek(0)
		try:
			while 1:
				img.seek(img.tell()+1)
				frame = img.copy()
				frame = frame.rotate(theta)
				output.append(frame)
				
		except EOFError:
			pass

#Save the first frame as a gif, with all subsequent frames appended. (just fucking saves it)
#also set gif to loop and not maintain frame data
output[0].save('out.gif', save_all=True, append_images=output[1:], loop=0, disposal=2)