import math
import random

XRES = 1000
YRES = 500 

f = open("pic.ppm", 'w')

f.write("P3\n")
f.write(str(XRES) + " " + str(YRES) + " 255\n")

''' RANDOM STROKES '''
RAND = 4  # smaller for larger color strokes

r = 0
b = 0
g = 0
for i in range(XRES):
	for j in range(YRES):
		f.write(str(r%256)+" "+str(g%256)+" "+str(b%256)+"\n")
		r += random.randrange(RAND)
		b += random.randrange(RAND)
		g += random.randrange(RAND)

''' Totally Random Colors
for i in range(XRES):
	for j in range(YRES):
		s = ""
		for k in range(3):
			s += str(random.randrange(256)) + " "
		f.write(s+"\n")
'''

f.close()
