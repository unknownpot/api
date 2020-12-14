import json
import pandas as pd 

t=pd.read_csv("ID.csv").values

print(t.reshape(-1,))

print(t.shape)