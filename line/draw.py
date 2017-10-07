from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
	x = x0
	y = y0
	dx = x1 - x0
	dy = y1 - y0
	
	# flip octants 3,4,5,6
	if (dx < 0):
		draw_line( screen, x1, y1, x0, y0, color )
		return

	if (dx != 0):
		slope = 1.0 * dy / dx
	else:
		if (dy < 0):
			draw_line( screen, x1, y1, x0, y0, color )
		else:
			while (y <= y1):
				plot(screen, color, x, y)
				y += 1
		return
	
	if get_octant(slope) == 1:
		D = 2 * dy - dx
		while (x <= x1):
			plot(screen, color, x, y)
			if (D > 0):
				y += 1
				D -= 2 * dx
			x += 1
			D += 2 * dy 

	elif get_octant(slope) == 2:
		D = dy - 2 * dx
		while (y <= y1):
			plot(screen, color, x, y)
			if (D < 0):
				x += 1
				D += 2 * dy
			y += 1
			D -= 2 * dx
	
	elif get_octant(slope) == 8:
		D = 2 * dy + dx
		while (x <= x1):
			plot(screen, color, x, y)
			if (D < 0):
				y -= 1
				D += 2 * dx
			x += 1
			D += 2 * dy
	
	elif get_octant(slope) == 7:
		D = dy + 2 * dx
		while (y >= y1):
			plot(screen, color, x, y)
			if (D > 0):
				x += 1
				D += 2 * dy
			y -= 1
			D += 2 * dx


def get_octant( slope ):
	'''
	4\3|2/1
	5/6|7\8
	'''
	if slope > 0 and slope <= 1:
		return 1
	elif slope > 1:
		return 2
	elif slope < -1:
		return 7
	else:
		return 8
