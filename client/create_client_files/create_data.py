import pandas as pd
import numpy as np

# create data 
df = pd.DataFrame(np.random.randint(1,255,size=(11000, 3)), columns=list('xyz'))
df.index.name='index'  
df.to_csv('data.test', sep=' ')
 
# set params from task
df = pd.read_csv('data.test', sep=' ')
df['i'] = df['index'] 
 
new_df = pd.DataFrame(df, columns = ["x", "y", "z", "i"]) 
 
new_df.to_csv('data.test', sep=' ', index=False)