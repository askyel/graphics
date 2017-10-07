import math

def make_translate( x, y, z ):
	matrix = new_matrix( 4, 4 )
	ident(matrix)
	matrix[0][3] = x
	matrix[1][3] = y
	matrix[2][3] = z
	return matrix

def make_scale( x, y, z ):
	matrix = new_matrix( 4, 4 )
	ident(matrix)
	matrix[0][0] = x
	matrix[1][1] = y
	matrix[2][2] = z
	return matrix
    
def make_rotX( theta ):   
	matrix = new_matrix( 4, 4 )
	rad = math.radians( theta )
	matrix[0][0] = 1
	matrix[1][1] = math.cos( rad )
	matrix[1][2] = -1 * math.sin( rad )
	matrix[2][1] = math.sin( rad )
	matrix[2][2] = math.cos( rad )
	return matrix

def make_rotY( theta ):
	matrix = new_matrix( 4, 4 )
	rad = math.radians( theta )
	matrix[0][0] = math.cos( rad )
	matrix[0][2] = math.sin( rad )
	matrix[1][1] = 1
	matrix[2][0] = -1 * math.sin( rad )
	matrix[2][2] = math.cos( rad )
	return matrix

def make_rotZ( theta ):
	matrix = new_matrix( 4, 4 )
	rad = math.radians( theta )
	matrix[0][0] = math.cos( rad )
	matrix[0][1] = -1 * math.sin( rad )
	matrix[1][0] = math.sin( rad )
	matrix[1][1] = math.cos( rad )
	matrix[2][2] = 1
	return matrix

def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m

def print_matrix( matrix ):
	rows = len(matrix) 
	cols = len(matrix[0])
	for r in range( rows ):
		s = "| " + str(matrix[r][0])
		for c in range( 1, cols ):
			s += ", " + str(matrix[r][c])
		s += " |"
		print( s )

def ident( matrix ):
	rows = len(matrix) 
	cols = len(matrix[0])
	for r in range( rows ):
		for c in range( cols ):
			if r == c:
				matrix[r][c] = 1
			else:
				matrix[r][c] = 0

def scalar_mult( matrix, x ):
	rows = len(matrix) 
	cols = len(matrix[0])
	for r in range( rows ):
		for c in range( cols ):
			matrix[r][c] *= x 

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
	rows = len(m1)
	cols = len(m2[0])
	nm = new_matrix( rows, cols )
	l = len(m2)
	for r in range( rows ):
		for c in range( cols ):
			dot_prod = 0
			for i in range( l ):
				dot_prod += m1[r][i] * m2[i][c]
			nm[r][c] = dot_prod
	return nm

