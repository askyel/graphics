from display import *
from draw import *

screen = new_screen()

edges = new_matrix( 4, 0 )

color = [ 255, 0, 0 ]
for ang in range(90):
    xval = int(XRES * math.sin(math.radians(ang)))
    yval = int(YRES * math.cos(math.radians(ang)))
    x0 = XRES - xval
    y0 = yval
    x1 = xval
    y1 = YRES - yval
    add_edge( edges, x0, y0, 0, x1, y1, 0 )
    rot = make_rotX(1)
    edges = matrix_mult( rot, edges )
draw_lines( edges, screen, color )
'''
color = [ 0, 255, 0 ]
for ang in range(90, 180):
    xval = int(XRES * math.sin(math.radians(ang)))
    yval = int(YRES * math.cos(math.radians(ang)))
    x0 = XRES - xval
    y0 = yval
    x1 = xval
    y1 = YRES - yval
    add_edge( edges, x0, y0, 0, x1, y1, 0 )
    rot = make_rotX(1)
    edges = matrix_mult( rot, edges )
draw_lines( edges, screen, color )

color = [ 0, 0, 255 ]
for ang in range(180, 270):
    xval = int(XRES * math.sin(math.radians(ang)))
    yval = int(YRES * math.cos(math.radians(ang)))
    x0 = XRES - xval
    y0 = yval
    x1 = xval
    y1 = YRES - yval
    add_edge( edges, x0, y0, 0, x1, y1, 0 )
    rot = make_rotX(1)
    edges = matrix_mult( rot, edges )
draw_lines( edges, screen, color )

color = [ 255, 255, 255 ]
for ang in range(270, 360):
    xval = int(XRES * math.sin(math.radians(ang)))
    yval = int(YRES * math.cos(math.radians(ang)))
    x0 = XRES - xval
    y0 = yval
    x1 = xval
    y1 = YRES - yval
    add_edge( edges, x0, y0, 0, x1, y1, 0 )
    rot = make_rotX(1)
    edges = matrix_mult( rot, edges )
draw_lines( edges, screen, color )
'''

'''
matrix = new_matrix(4,4)
print("IDENTITY MATRIX")
ident( matrix )
print_matrix( matrix )
print("\n")

matrix[0][1] = 2
matrix[1][0] = 3
print("SCALED MATRIX")
print("original matrix")
print_matrix( matrix )
scalar_mult( matrix, 3 )
print("multiplied by 3")
print_matrix( matrix ) 
print("\n")

print("MATRIX MULTIPLICATION")
print("first matrix")
m1 = new_matrix(2,3)
for i in range(6):
	m1[i/3][i%3] = i+1
print_matrix( m1 )
print("second matrix")
m2 = new_matrix(3,2)
for i in range(6):
	m2[i/2][i%2] = i+7
print_matrix( m2 )
print("product matrix")
m2 = matrix_mult( m1, m2 )
print_matrix( m2 )
print("\n")

print("TRANSLATION MATRIX")
matrix = make_translate( 5, 3, 2 )
print_matrix( matrix )
print("\n")

print("SCALAR MATRIX")
matrix = make_scale( 5, 3, 2 )
print_matrix( matrix )
print("\n")

print("ROTATION X MATRIX")
print("original matrix")
matrix = new_matrix(3,1)
matrix[0][0] = 1
matrix[1][0] = 2
matrix[2][0] = 3
print_matrix( matrix )
print("rotated matrix")
rot = make_rotX( 90 )
matrix = matrix_mult( rot, matrix )
print_matrix( matrix )
print("\n")
'''

display(screen)
