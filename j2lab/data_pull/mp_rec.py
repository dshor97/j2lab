import os
from matminer.data_retrieval.retrieve_MP import MPDataRetrieval
import pandas as pd

if not os.path.exists('data'):
	os.makedirs('data')

cursor = MPDataRetrieval(api_key='ywhDLoCAd3HWqfVs')
df_mp = cursor.get_dataframe(criteria='NaCl', properties=['pretty_formula',
'unit_cell_formula',
'icsd_ids',
'energy',
'energy_per_atom',
'volume',
'density',
'nsites',
'elements',
'nelements',
#'spacegroup',
#'initial_structure',
#'final_structure',
#'structure',
# 'cif',
'formation_energy_per_atom',
'e_above_hull','elasticity',
'piezo',
'diel',
'is_hubbard',
'hubbards',
'is_compatible',
'band_gap',
# 'dos',
#'bandstructure',
#'bandstructure_uniform',
'entry',
'total_magnetization'])

with open('data/test.csv', 'w') as file:
	file.write(df_mp.to_csv(index=False)) 
