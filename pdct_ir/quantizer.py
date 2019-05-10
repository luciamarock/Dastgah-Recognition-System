# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:50:09 2018

@author: luciamarock

"""




def Quantizer(ref_pitch, num_int, freq_vect):
    """
    this program adds two numbers and return the result
    
    """
    lowest=ref_pitch/float(16)
    step=pow(2,(1/float(num_int)))
    '''dim=len(y)
    y=x/dim'''
    y=[]
    for o in range(5):
        y.append(lowest*pow(2,o))
        for d in range(1,num_int):
            y.append(float(lowest*pow(2,o)*pow(step,d)))
    
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