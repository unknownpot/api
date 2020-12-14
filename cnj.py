import json
import requests
import pandas as pd

url="http://api.icndb.com/jokes/json?"


pr={
"value":""
}

r=requests.get(url,params=pr)

d=r.content

p=json.loads(d)

m=p["value"]

t=pd.read_csv("ID.csv").values

t=t.reshape(-1,)

a_jokes=[]
for i in range(len(m)):
    if(m[i]['id'] in t):
        joke=m[i]['joke']
        a_jokes.append(joke)

df=pd.DataFrame({'ID':t, 'joke': a_jokes})
df.to_csv("jokes.csv",index=False)