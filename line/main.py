from display import *
from draw import *
import math

screen = new_screen()

for ang in range(90):
	xval = int(XRES * math.sin(math.radians(ang)))
	yval = int(YRES * math.cos(math.radians(ang)))
	x0 = XRES - xval
	y0 = yval
	x1 = xval
	y1 = YRES - yval 
	colval = MAX_COLOR*ang/90
	color = [colval, 0, MAX_COLOR-colval]
	draw_line(screen, x0, y0, x1, y1, color)

display(screen)
