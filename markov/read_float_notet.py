# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 16:22:11 2018

@author: luciamarock
"""

from numpy import genfromtxt
#import matplotlib.pyplot as plt
#import math
import numpy as np
import os 
import sys

ns=98
radice = sys.argv[1]
nfile=sys.argv[2]

ext='.csv'
mtx='_matrix'
#mbid = 'RastPanjgah2_matrix'
mbid = radice+mtx
dataDir = './'
dataFile = os.path.join(dataDir, '{}.csv'.format(mbid))
# A[:,2] # returns the third columm
matrix=[]

for i in range (ns):
    #print(i)
    appoggio=[]
    for j in range (ns):
        appoggio.append(0.)    
    matrix.append(appoggio)
    

markov=np.array(matrix)

for i in range (int(nfile)):
    y='_%s' % str(i+1)
    nome = radice+y+ext
    #print('PROCESSING ' + nome)
    mydata = genfromtxt(nome, delimiter='\t')
    
    
    
    time=mydata[:,0]
    amp=mydata[:,1]
    #plt.plot(time,amp)
    
    
    x=[]
    y=[]
    stato=[]
    
    current=0
    for i in range(len(amp)):
        if amp[i]!=current:
            if amp[i]!=0:
                y.append(amp[i])
                x.append(time[i])
                current=amp[i]
            else:
                current=0
            
    #plt.plot(x,y,'s')
    
    for i in range (len(y)-1):
        #stato.append(abs(ns*math.log(y[i+1]/y[i],2)))
        if y[i]>y[i+1]:
            ratio=y[i]/y[i+1]
            a,b=divmod(ratio,1)
            a=int(a)
            if a >=2 and a<4:
                y[i]=y[i]/2
                ratio=y[i]/y[i+1]
            elif a >=4:
                y[i]=y[i]/4
                ratio=y[i]/y[i+1]
            stato.append((ratio-1)*ns)
            
        else:
            ratio=y[i+1]/y[i]
            a,b=divmod(ratio,1)
            a=int(a)
            if a >=2 and a<4:
                y[i+1]=y[i+1]/2
                ratio=y[i+1]/y[i]
            elif a>=4:
                y[i+1]=y[i+1]/4
                ratio=y[i+1]/y[i]
            stato.append((ratio-1)*ns)
            
        
        
    stato.append(0)
    for i in range(len(stato)):
        stato[i]=int(round(stato[i],0))%ns
    #plt.figure()
    #plt.plot(x,stato)
    #plt.plot(x,stato,'s')
    '''
    for j in range (len(y)-1):
        if y[j+1]>=y[j]:
            controprova.append(10+24*math.log(y[j+1]/y[j],2))
        else:
            controprova.append(10+24*math.log(y[j]/y[j+1],2))
            
    controprova.append(10)
    #plt.plot(x,controprova)
    '''
    #print(stato)
    
    
    '''
    entries=[]
    freq=[]
    for i in range(ns):
        entries.append(i)
        freq.append(0)
        
    for i in range (len(stato)):
        freq[stato[i]]=freq[stato[i]]+1
    max_freq=float(max(freq))
    if max_freq!=0:
        for i in range(len(freq)):
            freq[i]=freq[i]/max_freq
    
    plt.plot(entries,freq)
    plt.plot(entries,freq,'s')
    
    '''
    
    for i in range (len(stato)-1):
        markov[stato[i],stato[i+1]]=markov[stato[i],stato[i+1]]+1
#print(markov.T)
for i in range (ns):
    add=float(0)
    for j in range(ns):
        add=add+markov[i,j]
    #print(sum)
    if add !=0:
        for j in range(ns):
            markov[i,j]=markov[i,j]/add
            
#print(markov.T)

with open(dataFile, 'w+') as datafile_id:
    #writer=csv.writer(datafile_id, delimiter='\t')
    #writer.writerows(zip(timeSeries,pitchSeriesHz))
    np.savetxt(datafile_id, markov)
    
