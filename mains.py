import csv
import re
a=[]
b=[]
info=[]
def date(p):
  if (p[2]=="/" or p[1]=="/") and (p[4]=="/" or p[3]=="/" or p[5]=="/"):
    return 1
with open('dataset.csv', 'r') as file:
    reader = csv.reader(file,quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in reader:
      for i in row:
        a.append(i)       
for i in a:
  if len(i)>8:
    p=i[0:8]
    if date(p)==1:
      b.append(i)
def msg(k):
  ct=1
  for m in range(0,len(k)):
    if k[m]==":":
      ct=ct+1
    if ct==4:
      info.append(k[(m+1):])
      return 1


c=0
l=0
flag=0
s=[]
k=[]
se="s"
q=0
list=[]
for i in range(0,len(b)-1):
  #print("i",i,"b[i]",b[i])
  q=msg(b[i])
  #print("i",i,"k",k)
  for j in range(0,len(b[i])):
    if j < 7:
      if b[i][j]!=b[i+1][j]:
        flag=1
  if flag==1:
    c=c+1
    l=i
    s.append(c)
    #print(k)
    info.append(se)
    #print("..............")
  flag=0
print(info)

import spacy
  
nlp = spacy.load('en_core_web_sm')
  
sentence = "Jay wants to visit Jordan"
for sentence in info:
  doc = nlp(sentence)
  for ent in doc.ents:
    #print(ent.text, ent.start_char, ent.end_char, ent.label_)
    if ent.label_ =="PERSON":
       print(ent.text, ent.start_char, ent.end_char, ent.label_)