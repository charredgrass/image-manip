from PIL import Image

# im = Image.open("snow.gif")

output = []

with Image.open("snow.gif") as img:

	# img.seek(0)
	for theta in [0, -90, 180, 90]:
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
output[0].save('out.gif', save_all=True, append_images=output[1:], loop=0, disposal=2)