from modeller import *

env = Environ()

aln = Alignment(env)

# read the alignment file you used for modelling
aln.append(file='alignment.ali', alignment_format='PIR')

# calculate identity matrix
aln.id_table(matrix_file='identity_matrix.txt')