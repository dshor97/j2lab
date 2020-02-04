import os
import pandas as pd
from matminer.data_retrieval.retrieve_MDF import MDFDataRetrieval


if not os.path.exists('data'):
	os.makedirs('data')	

mdf_dr = MDFDataRetrieval(anonymous=True) 
df = mdf_dr.get_dataframe(criteria={'elements': ['Na', 'Cl']})

print(df)

with open('data/test.csv', 'w') as file:
	file.write(df.to_csv(index=False)) 
