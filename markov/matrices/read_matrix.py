# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 16:22:11 2018

@author: luciamarock
"""
from numpy import genfromtxt
import math
import subprocess
#import matplotlib.pyplot as plt

markov_data=genfromtxt('unknown_matrix.csv')
#RastPanjgah_matrix.csv
#print(markov_data.T)
ns=len(markov_data)
files_name=["Segah_matrix.csv","RastPanjgah_matrix.csv","Nava_matrix.csv","Mahour_matrix.csv","Homayun_matrix.csv","Chahargah_matrix.csv","Shur_matrix.csv"]
euclidean=[]
kullback=[]
Bhattacharyya=[]
SGPC=[]

for i in range (len(files_name)):
    name=files_name[i]
    db_matrix=genfromtxt(name)
    '''
    DIFFERENCES CUMULATION METHOD 
    '''
    '''
    diff=0
    for i in range (ns):
        for j in range (ns):
            diff=diff+abs(db_matrix[i,j]-markov_data[i,j])
            
    print("difference cumulation {1}".format(1,diff))
    '''
    #print('  euclidean distance')
    #search for the minimum
    diff=0
    for i in range (ns):
        for j in range (ns):
            diff=diff+pow(markov_data[i,j]-db_matrix[i,j],2)
            
    calc=math.sqrt(diff)
    euclidean.append(calc)
    
    #print('  Kullback-Leibler distance')
    #search for the minimum
    diff=0
    check=0
    for i in range (ns):
        for j in range (ns):
            r=0.
            if db_matrix[i,j]>=markov_data[i,j] and markov_data[i,j] !=0.:
               r=db_matrix[i,j]/markov_data[i,j]
               
            elif db_matrix[i,j] !=0:
                r=markov_data[i,j]/db_matrix[i,j]
                
            if r !=0:
                check=1
                diff=diff+markov_data[i,j]*math.log10(r)
            
    if diff>=0 and check<=0:
        diff=1000000.        
    kullback.append(diff)
    #print(diff)
    
    #print('  Bhattacharyya likelihood')
    #search for the maximum
    scalar=0
    for i in range (ns):
        for j in range(ns):
            scalar=scalar+math.sqrt((db_matrix[i,j]*markov_data[i,j]))
            
    Bhattacharyya.append(scalar)
    #print(scalar)
    '''
    STATES ABSOLUTE PROBABILITY CORRELATION METHOD 
    '''
    #SEARCH FOR THE MAX 
    data_prob=[]
    db_prob=[]
    entries=[]
    
    for i in range (ns):
        data_prob.append(0)
        db_prob.append(0)
        entries.append(i)    
        for j in range (ns):
            data_prob[i]=data_prob[i]+markov_data[j,i]
            db_prob[i]=db_prob[i]+db_matrix[j,i]
    #plt.figure()
    add_data=0
    add_db=0
    for i in range(ns):
        add_data=add_data+data_prob[i]
        add_db=add_db+db_prob[i]
    for i in range (ns):
        if add_data!=0 and add_db!=0:
            data_prob[i]=data_prob[i]/add_data
            db_prob[i]=db_prob[i]/add_db        
            
    corr=0
    for i in range (ns):
        corr=corr+data_prob[i]*db_prob[i]        
      
    SGPC.append(corr)
    #print("states global probability correlation {1}".format(1,corr))    
nrows=100
nrows=int(subprocess.check_output(["./nrows.sh"]))
if nrows < 5:
    kullback[0]=0
log_row=[0, 0, 0, 0]
log_row[0]=euclidean.index(min(euclidean))
log_row[1]=kullback.index(min(kullback))
log_row[2]=Bhattacharyya.index(max(Bhattacharyya))
log_row[3]=SGPC.index(max(SGPC))

with open("results.log", "a") as f:    
    f.write(str(log_row[0]) + "\t" + str(log_row[1]) + "\t" + str(log_row[2]) + "\t" + str(log_row[3]) + "\t" + "\n")
    f.close()
'''
print("euclidean says ---> {1}".format(1,files_name[log_row[0]]))
print("kullback says ---> {1}".format(1,files_name[log_row[1]]))
print("Bhattacharyya says ---> {1}".format(1,files_name[log_row[2]]))
print("SGPC says ---> {1}".format(1,files_name[log_row[3]]))
'''
'''
plt.plot(entries,data_prob)
plt.plot(entries,data_prob,'s')

plt.plot(entries,db_prob)
plt.plot(entries,db_prob,'s')
'''
'''
print('  euclidean distance')
print(euclidean)
print('  Kullback-Leibler distance')
print(kullback)
print('  Bhattacharyya likelihood')
print(Bhattacharyya)
print("states global probability correlation")
print(SGPC)
'''