# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 11:43:51 2018

@author: luciamarock
"""






def Cleaner(history, freq_vect):
    """    
    this function clean the freq_vect on the basis of history (number of 
    consecutive samples with the same freq)    
    a frequency value is taken only if it is proven to be stable 
    
    """
    counter=0
    starting=-1
      

    for i in range (len(freq_vect)-history+1):
        check=0
        for j in range (history):
            if freq_vect[i]!=freq_vect[i+j]:
                check=1
                
        if check==0:
        
            if counter > 0:
            
                for z in range (1,counter):
                    freq_vect[starting+z]=freq_vect[starting]
            counter=0
            starting=-1
    
        elif starting==-1:
            starting=i
        
            counter = counter+1
            if i==(len(freq_vect)-history):
                for z in range (1,counter):
                    freq_vect[starting+z]=freq_vect[starting]
        
        else:
            counter = counter+1
        
            if i==(len(freq_vect)-history):
                for z in range (1,counter):
                    freq_vect[starting+z]=freq_vect[starting]

    for i in range(len(freq_vect)-2, len(freq_vect)):
        freq_vect[i]=0
    
    return freq_vect
    
    '''
    y=np.insert(y,0,20.0)
    end=[20000]
    y=np.concatenate((y,end),axis=None)
    '''