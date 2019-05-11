# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 16:22:11 2018

@author: luciamarock
"""
'''
this program perform the necessary statistics using the file results.log 
in order to present the results in the paper 
'''
from numpy import genfromtxt
import numpy as np
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
label=['Segah', 'RastPanjgah', 'Nava', 'Mahour', 'Homayun', 'Chahargah','Shur']
array = [[0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0]]
array=np.array(array)     
distance_type=["euclidean","kullback","Bhattacharyya","SGPC"]
parameters=["recall","specificity","precision","FPR","FNR","F1","accuracy"]

modes=genfromtxt('expected.log')
logfile=genfromtxt('results.log')

attesi=modes
metrica=logfile[:,2]

for i in range(len(attesi)):
    array[attesi[i],metrica[i]]=array[attesi[i],metrica[i]]+1
df_cm = pd.DataFrame(array, label, label)
sn.set(font_scale=1.2)
#plt.rcParams.update({'font.size': 40}) 
plt.figure(figsize = (11,8))
plt.title('Bhattacharyya likelihood',size=25)
sn.heatmap(df_cm, cmap="Greys", annot=True,annot_kws={"size": 15})
#l'errore è che un Mahour è stato classificato Nava 

vect=logfile[:,0]

dim=len(vect)


tp=0.
fp=0.
fn=0.
tn=0.
nsamp=73
#BUILD THE CONFUSION MATRIX 

confusion=np.array([[tp,fp,fn,tn],[0,0,0,0],[0,0,0,0],[0,0,0,0]])


for i in range (dim):
    for j in range (len(distance_type)):
        if modes[i] == logfile[i,j]:
            confusion[j,0]=confusion[j,0] + 1
            confusion[j,3]=confusion[j,3] + 6   
        else:
            confusion[j,1]=confusion[j,1] + 1
            confusion[j,2]=confusion[j,2] + 5
            #confusion[j,3]=confusion[j,3] + 1   
            
#print(confusion)

rec=0.1
spe=0.
pre=0.
fpr=0.
fnr=0.
funo=2*pre*rec/(pre+rec)
acc=0.

scores=np.array([[rec,spe,pre,fpr,fnr,funo,acc],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]])
for i in range (len(distance_type)):
    scores[i,0]=confusion[i,0]/(confusion[i,0]+confusion[i,2])
    scores[i,1]=confusion[i,3]/(confusion[i,3]+confusion[i,1])
    scores[i,2]=confusion[i,0]/(confusion[i,0]+confusion[i,1])
    scores[i,3]=confusion[i,1]/nsamp #(confusion[i,1]+confusion[i,3])
    scores[i,4]=confusion[i,2]/(confusion[i,2]+confusion[i,0])    
    funo=2*scores[i,2]*scores[i,0]/(scores[i,2]+scores[i,0])
    scores[i,5]=funo
    scores[i,6]=confusion[i,0]/nsamp
    #scores[i,6]=(confusion[i,0]+confusion[i,3])/(confusion[i,0]+confusion[i,1]+confusion[i,2]+confusion[i,3])
print(' ')
for i in range (len(distance_type)):
    for j in range (len(parameters)):    
        #print('{} {} = {}'.format(distance_type[i], parameters[j], scores[i,j]))
        with open("scores.res", "a") as f:
            f.write('{} {} = {}'.format(distance_type[i], parameters[j], scores[i,j]) + "\n")
            f.close()
print(' ')    
#print(scores)
plt.show()