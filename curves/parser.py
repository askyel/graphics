from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
	print "parsing script... \n"
	f = open( fname )
	while (1):
		line = f.readline().strip()
		if line == "":
			return
		
		if line == "line":
			args = f.readline().strip().split( " " )
			add_edge( points, float(args[0]), float(args[1]), float(args[2]), float(args[3]), float(args[4]), float(args[5]) )
		elif line == "circle":
			args = f.readline().strip().split( " " )
			add_circle( points, float(args[0]), float(args[1]), 0, float(args[2]), 1 )
		elif line == "hermite":
			args = f.readline().strip().split( " " )
			add_curve( points, float(args[0]), float(args[1]), float(args[2]), float(args[3]), float(args[4]), float(args[5]), float(args[6]), float(args[7]), 100, HERMITE_MODE )
			print "hermite added"
		elif line == "bezier":
			args = f.readline().strip().split( " " )
			add_curve( points, float(args[0]), float(args[1]), float(args[2]), float(args[3]), float(args[4]), float(args[5]), float(args[6]), float(args[7]), 100, BEZIER_MODE )
			print "bezier added"
		elif line == "ident":
			ident( transform )
		elif line == "scale":
			args = f.readline().strip().split( " " )
			m = make_scale( float(args[0]), float(args[1]), float(args[2]) )
			matrix_mult( m, transform )
		elif line == "translate":
			args = f.readline().strip().split( " " )
			m = make_translate( float(args[0]), float(args[1]), float(args[2]) )
			matrix_mult( m, transform )
		elif line == "xrotate":
			args = f.readline().strip().split( " " )
			m = make_rotX( math.radians( float(args[0] ) ) )
			matrix_mult( m, transform )
		elif line == "yrotate":
			args = f.readline().strip().split( " " )
			m = make_rotY( math.radians( float(args[0] ) ) )
			matrix_mult( m, transform )
		elif line == "zrotate":
			args = f.readline().strip().split( " " )
			m = make_rotZ( math.radians( float(args[0] ) ) )
			matrix_mult( m, transform )
		elif line == "apply":
			matrix_mult( transform, points )
		elif line == "display":
			clear_screen( screen )
			draw_lines( points, screen, color )
			display( screen )
		elif line == "save":
			print "saving file... \n"
			args = f.readline().strip().split( " " )
			clear_screen( screen )
			draw_lines( points, screen, color )
			save_ppm( screen, args[0] ) 
		else:
			print "unrecognized command: " + line + "\n"
	
	print "...done"


