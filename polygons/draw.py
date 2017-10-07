from display import *
from matrix import *
import math

MAX_STEPS = 150

def add_polygon( points, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point( points, x0, y0, z0 )
    add_point( points, x1, y1, z1 )
    add_point( points, x2, y2, z2 )

def draw_polygons( points, screen, color ):
    num = len(points)
    for i in range( 0, num, 3 ):
        P0x = points[i][0]
        P0y = points[i][1]
        P0z = points[i][2]
        P1x = points[i+1][0]
        P1y = points[i+1][1]
        P1z = points[i+1][2]
        P2x = points[i+2][0]
        P2y = points[i+2][1]
        P2z = points[i+2][2]
        # backface culling
        A = [ P1x - P0x, P1y - P0y, P1z - P0z ]
        B = [ P2x - P0x, P2y - P0y, P2z - P0z ]
        N = [ A[1]*B[2]-A[2]*B[1], A[2]*B[0]-A[0]*B[2], A[0]*B[1]-A[1]*B[0] ]
        V = [ 0, 0, -1 ]
        cross_prod = N[0]*V[0] + N[1]*V[1] + N[2]*V[2]
        if cross_prod < 0:
            # lines between P0-P1, P1-P2, P2-P0
            draw_line( screen, points[i][0], points[i][1], points[i+1][0], points[i+1][1], color )
            draw_line( screen, points[i+1][0], points[i+1][1], points[i+2][0], points[i+2][1], color )
            draw_line( screen, points[i+2][0], points[i+2][1], points[i][0], points[i][1], color )

def add_box( points, x, y, z, width, height, depth ):
    x1 = x + width
    y1 = y - height
    z1 = z - depth
    # add polygon faces
    add_polygon( points, x, y1, z, x1, y, z, x, y, z )
    add_polygon( points, x, y1, z, x1, y1, z, x1, y, z )
    add_polygon( points, x1, y1, z, x1, y, z1, x1, y, z )
    add_polygon( points, x1, y, z1, x1, y1, z, x1, y1, z1 )
    add_polygon( points, x1, y, z1, x1, y1, z1, x, y, z1 )
    add_polygon( points, x1, y1, z1, x, y1, z1, x, y, z1 )
    add_polygon( points, x, y1, z, x, y, z, x, y, z1 )
    add_polygon( points, x, y1, z1, x, y1, z, x, y, z1 )
    add_polygon( points, x1, y, z, x, y, z1, x, y, z )
    add_polygon( points, x1, y, z, x1, y, z1, x, y, z1 )
    add_polygon( points, x1, y1, z, x, y1, z1, x1, y1, z1 )
    add_polygon( points, x, y1, z1, x1, y1, z, x, y1, z )
        
def add_sphere( points, cx, cy, cz, r, step ):
    
    num_steps = MAX_STEPS / step
    temp = []

    generate_sphere( temp, cx, cy, cz, r, step )

    lat = -1
    lat_stop = num_steps
    longt_stop = num_steps
    
    while lat < lat_stop-1:
        longt = -1
        while longt < longt_stop-1:
            
            index = lat * num_steps + longt

            add_polygon( points, 
                         temp[index][0], temp[index][1], temp[index][2],
                         temp[index+1][0], temp[index+1][1], temp[index+1][2],
                         temp[index+num_steps][0], temp[index+num_steps][1], temp[index+num_steps][2] )
            add_polygon( points, 
                         temp[index+num_steps][0], temp[index+num_steps][1], temp[index+num_steps][2],
                         temp[index+1][0], temp[index+1][1], temp[index+1][2],
                         temp[index+num_steps+1][0], temp[index+num_steps+1][1], temp[index+num_steps+1][2] )

            longt+= 1
        lat+= 1

def generate_sphere( points, cx, cy, cz, r, step ):

    rotation = 0
    rot_stop = MAX_STEPS
    circle = 0
    circ_stop = MAX_STEPS

    while rotation < rot_stop:
        circle = 0
        rot = float(rotation) / MAX_STEPS
        while circle < circ_stop:
            
            circ = float(circle) / MAX_STEPS
            x = r * math.cos( 2 * math.pi * circ ) + cx
            y = r * math.sin( 2 * math.pi * circ ) * math.cos( 2 * math.pi * rot ) + cy
            z = r * math.sin( 2 * math.pi * circ ) * math.sin( 2 * math.pi * rot ) + cz
            
            add_point( points, x, y, z )

            circle+= step
        rotation+= step

def add_torus( points, cx, cy, cz, r0, r1, step ):
    
    num_steps = MAX_STEPS / step
    temp = []

    generate_torus( temp, cx, cy, cz, r0, r1, step )

    lat = -1
    lat_stop = num_steps
    longt_stop = num_steps
    
    while lat < lat_stop-1:
        longt = -1
        while longt < longt_stop-1:
            
            index = lat * num_steps + longt
            add_polygon( points, 
                         temp[index][0], temp[index][1], temp[index][2],
                         temp[index+1][0], temp[index+1][1], temp[index+1][2],
                         temp[index+num_steps][0], temp[index+num_steps][1], temp[index+num_steps][2] )
            add_polygon( points,
                         temp[index+num_steps][0], temp[index+num_steps][1], temp[index+num_steps][2],
                         temp[index+1][0], temp[index+1][1], temp[index+1][2],
                         temp[index+num_steps+1][0], temp[index+num_steps+1][1], temp[index+num_steps+1][2] ) 

            longt+= 1
        lat+= 1

def generate_torus( points, cx, cy, cz, r0, r1, step ):

    rotation = 0
    rot_stop = MAX_STEPS
    circle = 0
    circ_stop = MAX_STEPS

    while rotation < rot_stop:
        circle = 0
        rot = float(rotation) / MAX_STEPS
        while circle < circ_stop:
            
            circ = float(circle) / MAX_STEPS
            x = (math.cos( 2 * math.pi * rot ) *
                 (r0 * math.cos( 2 * math.pi * circ) + r1 ) + cx)
            y = r0 * math.sin(2 * math.pi * circ) + cy
            z = (math.sin( 2 * math.pi * rot ) *
                 (r0 * math.cos(2 * math.pi * circ) + r1))
            
            add_point( points, x, y, z )

            circle+= step
        rotation+= step



def add_circle( points, cx, cy, cz, r, step ):
    x0 = r + cx
    y0 = cy

    t = step
    while t<= 1:
        
        x = r * math.cos( 2 * math.pi * t ) + cx
        y = r * math.sin( 2 * math.pi * t ) + cy

        add_edge( points, x0, y0, cz, x, y, cz )
        x0 = x
        y0 = y
        t+= step
    add_edge( points, x0, y0, cz, cx + r, cy, cz )

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    xcoefs = generate_curve_coefs( x0, x1, x2, x3, curve_type )
    ycoefs = generate_curve_coefs( y0, y1, y2, y3, curve_type )
        
    t =  step
    while t <= 1:
        
        x = xcoefs[0][0] * t * t * t + xcoefs[0][1] * t * t + xcoefs[0][2] * t + xcoefs[0][3]
        y = ycoefs[0][0] * t * t * t + ycoefs[0][1] * t * t + ycoefs[0][2] * t + ycoefs[0][3]

        add_edge( points, x0, y0, 0, x, y, 0 )
        x0 = x
        y0 = y
        t+= step

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

