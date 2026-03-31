from modeller import *
from modeller.automodel import *

env = environ()
a = automodel(env,
              alnfile  = 'alignment.ali',   # your alignment file
              knowns   = '5IKQ',           # template name
              sequence = 'COX2_4')         # target name
a.starting_model= 1
a.ending_model  = 5
a.make()