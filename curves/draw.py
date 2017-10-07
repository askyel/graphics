from display import *
from matrix import *
import math

def add_circle( points, cx, cy, cz, r, step ):
	t = 0
	x0 = cx + r * math.sin( math.radians(t) )
	y0 = cy + r * math.cos( math.radians(t) )
	for t in range( 0, 360, step ):
		x = cx + r * math.sin( math.radians(t+step) )
		y = cy + r * math.cos( math.radians(t+step) )
		add_edge( points, x0, y0, 0, x, y, 0 )
		x0 = x
		y0 = y

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
	xco = generate_curve_coefs( x0, x1, x2, x3, curve_type )
	yco = generate_curve_coefs( y0, y1, y2, y3, curve_type )
	t = 0
	x = xco[0][0]*math.pow(t,3) + xco[0][1]*math.pow(t,2) + xco[0][2]*t + xco[0][3]
	y = yco[0][0]*math.pow(t,3) + yco[0][1]*math.pow(t,2) + yco[0][2]*t + yco[0][3]
	for t in range(step):
		T = 1/(t+1)
		X = xco[0][0]*math.pow(T,3) + xco[0][1]*math.pow(T,2) + xco[0][2]*T + xco[0][3]
		Y = yco[0][0]*math.pow(T,3) + yco[0][1]*math.pow(T,2) + yco[0][2]*T + yco[0][3]
		add_edge( points, x, y, 0, X, Y, 0 )
		x = X
		y = Y
	print "curve adding done"
 
def draw_lines( matrix, screen, color ):
    if len( matrix ) < 2:
        print "Need at least 2 points to draw a line"
        
    p = 0
    while p < len( matrix ) - 1:
        draw_line( screen, matrix[p][0], matrix[p][1],
                   matrix[p+1][0], matrix[p+1][1], color )
        p+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )


def draw_line( screen, x0, y0, x1, y1, color ):
    dx = x1 - x0
    dy = y1 - y0
    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp
    
    if dx == 0:
        y = y0
        while y <= y1:
            plot(screen, color,  x0, y)
            y = y + 1
    elif dy == 0:
        x = x0
        while x <= x1:
            plot(screen, color, x, y0)
            x = x + 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            d = d - dy
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            d = d - dx
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            d = d + dy
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx

