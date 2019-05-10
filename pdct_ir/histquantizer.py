# -*- coding: utf-8 -*-

"""
Created on Thu Oct 25 15:50:09 2018

@author: luciamarock

"""
import numpy as np



def Histquantizer(tonic, cents, y, freq_vect):
    """    
    this program adds two numbers and return the result
    y is cets_vector
    
    """
    cents = float(cents)
        
    for q in range(len(y)):
        y[q]=tonic*pow(2.0,(y[q]/cents))
    y=np.insert(y,0,20.0)
    end=[20000]
    y=np.concatenate((y,end),axis=None)
    for q in range(len(freq_vect)):
        for t in range(len(y)-1):
            if freq_vect[q]>=y[t] and freq_vect[q]<=y[t+1]:
                if (freq_vect[q]-y[t])>=(y[t+1]-freq_vect[q]):
                    freq_vect[q]=y[t+1]
                else:
                    freq_vect[q]=y[t]    
    return freq_vect
    
    
'''
ref_pitch=440
num_int=24
x = []
azzo=Quantizer(ref_pitch,num_int,x)

for p in range(1,len(azzo)+1):
    x.append(p)


#dim=len(azzo)
#print (azzo)
plt.plot(x,azzo)
plt.show()
'''