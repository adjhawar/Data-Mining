import pandas as pd
import numpy as np

#removing the null rows
f="responses.csv"
df=pd.read_csv(f)
df1=df.dropna(axis=0)
df1.to_csv("non_null_responses.csv",index=False)

print(df1.corr())
