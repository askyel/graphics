"""========== script.py ==========

  This is the only file you need to modify in order
  to get a working mdl project (for now).

  my_main.c will serve as the interpreter for mdl.
  When an mdl script goes through a lexer and parser, 
  the resulting operations will be in the array op[].

  Your job is to go through each entry in op and perform
  the required action from the list below:

  frames: set num_frames for animation

  basename: set name for animation

  vary: manipluate knob values between two given frames
        over a specified interval

  set: set a knob to a given value
  
  setknobs: set all knobs to a given value

  push: push a new origin matrix onto the origin stack
  
  pop: remove the top matrix on the origin stack

  move/scale/rotate: create a transformation matrix 
                     based on the provided values, then 
		     multiply the current top of the
		     origins stack by it.

  box/sphere/torus: create a solid object based on the
                    provided values. Store that in a 
		    temporary matrix, multiply it by the
		    current top of the origins stack, then
		    call draw_polygons.

  line: create a line based on the provided values. Store 
        that in a temporary matrix, multiply it by the
	current top of the origins stack, then call draw_lines.

  save: call save_extension with the provided filename

  display: view the image live
  
  jdyrlandweaver
  ========================="""



import mdl
from display import *
from matrix import *
from draw import *

basename = "DEFAULT"
num_frames = 1
knobs = []


"""======== first_pass( commands, symbols ) ==========

  Checks the commands array for any animation commands
  (frames, basename, vary)
  
  Should set num_frames and basename if the frames 
  or basename commands are present

  If vary is found, but frames is not, the entire
  program should exit.

  If frames is found, but basename is not, set name
  to some default value, and print out a message
  with the name being used.

  jdyrlandweaver
  ==================== """
def first_pass( commands ):
	global basename
	global num_frames
	hasFrames = False
	hasVary = False
	for command in commands:
		if command[0] == "frames":
			num_frames = command[1]
			hasFrames = True
		elif command[0] == "basename":
			basename = command[1]
		elif command[0] == "vary":
			hasVary = True
	if basename == "DEFAULT":
		print "Basename set to " + basename
	if not hasFrames:
		exit()
        

"""======== second_pass( commands ) ==========

  In order to set the knobs for animation, we need to keep
  a seaprate value for each knob for each frame. We can do
  this by using an array of dictionaries. Each array index
  will correspond to a frame (eg. knobs[0] would be the first
  frame, knobs[2] would be the 3rd frame and so on).

  Each index should contain a dictionary of knob values, each
  key will be a knob name, and each value will be the knob's
  value for that frame.

  Go through the command array, and when you find vary, go 
  from knobs[0] to knobs[frames-1] and add (or modify) the
  dictionary corresponding to the given knob with the
  appropirate value. 
  ===================="""
def second_pass( commands, num ):
	global knobs
	for i in range(num):
		if i >= len(knobs):
			knobs.append({})
		else:
			knobs[i] = {}
	for command in commands:
		if command[0] == "vary":
			knob = command[1]
			fo = int(command[2])
			fi = int(command[3])
			vo = int(command[4])
			vi = int(command[5])
			for i in range( fo, fi+1 ):
				val = vo + 1.0 * (i-fo) * (vi-vo) / (fi-fo)
				knobs[i][knob] = val


def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return   

    global basename
    global num_frames
    global knobs
     
    first_pass( commands )
    if num_frames > 1:
    	second_pass( commands, num_frames )
    
    for i in range( num_frames ):

    	stack = [ tmp ]
    	screen = new_screen()

    	for command in commands:
	        if command[0] == "pop":
	            stack.pop()
	            if not stack:
	                stack = [ tmp ]

	        if command[0] == "push":
	            stack.append( stack[-1][:] )

	        if command[0] == "save":
	            save_extension(screen, command[1])

	        if command[0] == "display":
	            display(screen)

	        if command[0] == "sphere":
	            m = []
	            add_sphere(m, command[1], command[2], command[3], command[4], 5)
	            matrix_mult(stack[-1], m)
	            draw_polygons( m, screen, color )

	        if command[0] == "torus":
	            m = []
	            add_torus(m, command[1], command[2], command[3], command[4], command[5], 5)
	            matrix_mult(stack[-1], m)
	            draw_polygons( m, screen, color )

	        if command[0] == "box":                
	            m = []
	            add_box(m, *command[1:])
	            matrix_mult(stack[-1], m)
	            draw_polygons( m, screen, color )

	        if command[0] == "line":
	            m = []
	            add_edge(m, *command[1:])
	            matrix_mult(stack[-1], m)
	            draw_lines( m, screen, color )

	        if command[0] == "bezier":
	            m = []
	            add_curve(m, command[1], command[2], command[3], command[4], command[5], command[6], command[7], command[8], .05, 'bezier')
	            matrix_mult(stack[-1], m)
	            draw_lines( m, screen, color )

	        if command[0] == "hermite":
	            m = []
	            add_curve(m, command[1], command[2], command[3], command[4], command[5], command[6], command[7], command[8], .05, 'hermite')
	            matrix_mult(stack[-1], m)
	            draw_lines( m, screen, color )

	        if command[0] == "circle":
	            m = []
	            add_circle(m, command[1], command[2], command[3], command[4], .05)
	            matrix_mult(stack[-1], m)
	            draw_lines( m, screen, color )

	        if command[0] == "move": 
	        	if command[4] == None or command[4] not in knobs[i]:
	        		mult = 1
	        	else:
	        		mult = knobs[i][command[4]]

	        	xval = command[1] * mult
	        	yval = command[2] * mult
	        	zval = command[3] * mult

	        	t = make_translate(xval, yval, zval)
	        	matrix_mult( stack[-1], t )
	        	stack[-1] = t

	        if command[0] == "scale":
	        	if command[4] == None or command[4] not in knobs[i]:
	        		mult = 1
	        	else:
	        		mult = knobs[i][command[4]]

	        	xval = command[1] * mult
	        	yval = command[2] * mult
	        	zval = command[3] * mult

	        	t = make_scale(xval, yval, zval)
	        	matrix_mult( stack[-1], t )
	        	stack[-1] = t
	            
	        if command[0] == "rotate":
	        	if command[3] == None or command[3] not in knobs[i]:
	        		mult = 1
	        	else:
	        		mult = knobs[i][command[3]]
	        	angle = command[2] * (math.pi / 180) * mult

	        	if command[1] == 'x':
	        		t = make_rotX( angle )
	        	elif command[1] == 'y':
	        		t = make_rotY( angle )
	        	elif command[1] == 'z':
	        		t = make_rotZ( angle )

	        	matrix_mult( stack[-1], t )
	        	stack[-1] = t

		save_extension(screen, "anim/" + basename + str(i))
            
