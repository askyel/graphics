import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    transform = new_matrix(4,1)
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    stack = [ tmp ]
    screen = new_screen()
        
    for command in commands:
        print command
        c = command[0]

        if c == "push":
        	stack = [ stack[0] ] + stack

        elif c == "pop":
        	stack.pop()

        elif c == "rotate":
        	axis = command[1]
        	deg = command[2] * ( math.pi / 180 )
        	knob = command[3]
        	if axis == 'x':
        		tmp = make_rotX( deg )
        	elif axis == 'y':
        		tmp = make_rotY( deg )
        	elif axis == 'z':
        		tmp = make_rotZ( deg )
        	matrix_mult( stack[0], tmp )
        	#copy_matrix( tmp, stack[0] )

        elif c == "scale":
        	tmp = make_scale( command[1], command[2], command[3] )
        	matrix_mult( stack[0], tmp )

        elif c == "move":
        	tmp = make_translate( command[1], command[2], command[3] )
        	matrix_mult( stack[0], tmp )

        elif c == "sphere":
        	add_sphere( transform, command[1], command[2], command[3], command[4], 5 )
        	matrix_mult( stack[0], transform )
        	draw_polygons( transform, screen, color )
        	ident( transform )

        elif c == "torus":
        	add_torus( transform, command[1], command[2], command[3], command[4], command[5], 5 )
        	matrix_mult( stack[0], transform )
        	draw_polygons( transform, screen, color )
        	ident( transform )

        elif c == "box":
        	add_box( transform, command[1], command[2], command[3], command[4], command[5], command[6] )
        	matrix_mult( stack[0], transform )
        	draw_polygons( transform, screen, color )
        	ident( transform )

        elif c == "line":
        	add_edge( transform, command[1], command[2], command[3], command[4], command[5], command[6] )
        	matrix_mult( stack[0], transform )
        	draw_lines( transform, screen, color )
        	ident( transform )

        elif c == "display":
        	display( screen )

        elif c == "save":
        	save_extension( screen, command[1] )

        else:
        	print "other"
