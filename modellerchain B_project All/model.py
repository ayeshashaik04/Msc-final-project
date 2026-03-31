from modeller import *
from modeller.automodel import *

# Initialize the MODELLER environment
env = environ()

# Create the automodel object
a = automodel(
    env,
    alnfile  = 'alignment.ali',            # your corrected PIR alignment
    knowns   = '5IKQ',                     # template name in PIR
    sequence = 'COX2_All_Mutations'        # target name in PIR
)

# Generate multiple models
a.starting_model = 1
a.ending_model   = 5  # generate 5 models

# Build the models
a.make()