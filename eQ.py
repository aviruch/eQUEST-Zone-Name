import os
import glob
import re
import csv
import sys
import shutil #to copy file

filename= raw_input("Enter file name to convert with extension\n")
f=open(filename,"r")
text = f.read()
tuple=re.findall(r'(.*)[\s]=[\s]SPACE\s',text,re.M)
#print tuple
tuple1=[]

for i in tuple:
    tuple1.append(i.strip('"')+"_ZN")

print tuple1

pat = '["](.*)["][\s]=[\s]ZONE'

#"EL1 Zn (G.1)" = ZONE   
tuple2=re.findall(pat,text,re.M)
#print tuple2                  


d = dict(zip(tuple2,tuple1))
print d


filename1= "Changed_"+filename
shutil.copy2(filename,filename1)

f1=open(filename1,"w")
for i,j in d.iteritems():
    text=text.replace(i,j)

f1.write(text)
f1.close


f.close()










        
