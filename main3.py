import pandas as pd
import operator
df = pd.read_csv('file_example_CSV_5000.csv')
df.drop(['Unnamed: 0', 'Age', 'Date', 'Id'], axis = 1, inplace = True)
print(df)
d1=dict()
header=list(df.columns.values)
fields=[]
for field in header:
  for i in range(5000):
    for c in df[field][i]:
      if c in d1:
        d1[c]= d1[c]+1
      else:
        d1[c]=1
#print (d1)
sdd1 = dict( sorted(d1.items(), key=operator.itemgetter(1),reverse=True))
#print(sdd1)
res=list()
outkey=list()
out=dict()
value=list(sdd1.values())
keys=list(sdd1.keys())
r=0
for x in value:
  for k,v in sdd1.items():
    if x==r:
      break
    if v == x:
      res.append(k)
  r=x
  res1=sorted(res)
  res.clear()
  for l in res1:
    outkey.append(l)
#print(keys)
#print (outkey)
out = {}
for key in outkey:
    for valu in value:
        out[key] = valu
        value.remove(valu)
        break
print ("Resultant dictionary is : " +  str(out))