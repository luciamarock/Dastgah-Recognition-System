# -*- coding: utf-8 -*-

"""
Created on Thu Oct 25 15:50:09 2018

@author: luciamarock

"""
import soundfile as sf
import numpy as np
#import matplotlib.pyplot as plt
import math

def Tonicext(wav_path):
    '''
    this function calculate the highest peak in the fft of the signal 
    this is used as reference tone in the main algorithm 
    '''
    data, samplerate = sf.read(wav_path)
    #sf.write('new_file.flac', data, samplerate)
    #print (samplerate)
    limit=samplerate*10
    if len(data)>=limit:
        data=data[:limit]
    
    ccount=len(data)
    #if ccount>=limit:
     #   ccount=limit
    abscissa=[]
    for i in range (ccount):
        abscissa.append(i)


    npspettro=np.fft.fft(np.array(data))
    npmodulo=[]
    for i in range (ccount):
        npmodulo.append(math.sqrt(pow(npspettro[i].real,2)+pow(npspettro[i].imag,2)))
    bins=float(samplerate)/ccount

    frequenze=[]
    ampiezze=[]
    for i in range (ccount/2):
        ampiezze.append(npmodulo[i])
        frequenze.append(bins/2.+i*bins)

    tonic = frequenze[ampiezze.index(max(ampiezze))]
    return tonic
'''
plt.subplot(211)
plt.plot(abscissa,data)
plt.subplot(212)
plt.plot(frequenze,ampiezze)
'''
#print(frequenze[ampiezze.index(max(ampiezze))])  

