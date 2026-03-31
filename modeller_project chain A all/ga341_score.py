from modeller import *
from modeller.scripts import complete_pdb

env = Environ()

models = [
'COX2_All_Mutations.B99990001.pdb',
'COX2_All_Mutations.B99990002.pdb',
'COX2_All_Mutations.B99990003.pdb',
'COX2_All_Mutations.B99990004.pdb',
'COX2_All_Mutations.B99990005.pdb'
]

for m in models:
    mdl = complete_pdb(env, m)
    print("Model:", m)
    print("GA341 Score:", mdl.assess_ga341())