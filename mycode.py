import pandas as pd
import os
#create a dataframe with column names
data ={"Name":["Alice","Bob","Charlie"],
       'Age':[25,30,35],
       'City':['Newyork','Los Angeles','Chicago']}
df=pd.DataFrame(data)
new_row_loc={'Name':'gf', 'Age':20,'City':'London'}
df.loc[len(df.index)]=new_row_loc
new_row_loc2={'Name':'gf2', 'Age':25,'City':'London'}
df.loc[len(df.index)]=new_row_loc2
data_dir='data'
os.makedirs(data_dir,exist_ok=True)
file_path=os.path.join(data_dir,'sample_data.csv')  
df.to_csv(file_path,index=False)   
print(f"Csv file saved to {file_path}")         