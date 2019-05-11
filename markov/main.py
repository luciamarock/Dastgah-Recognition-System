# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 16:22:11 2018

@author: luciamarock
"""

import os
import subprocess

names=["Segah","RastPanjgah","Nava","Mahour","Homayun","Chahargah","Shur"]
nfiles=[]

for i in range (len(names)):
    value=int(subprocess.check_output(["./search.sh","{}".format(names[i])]))
    nfiles.append(value)
tot=0
for i in range(len(nfiles)):
    tot=tot+nfiles[i]
os.system('./createlog.sh')
    
for i in range(len(names)):
    for j in range (len(names)):
        if names[i]!=names[j]:
            print(' ' )
            #os.system('./matrices.sh {}'.format(names[j]))
        else:
            print('name = {}, nfiles = {}'.format(names[i],nfiles[i]))
            for k in range(nfiles[i]):
                #print('processing {}_{}'.format(names[i],k+1))
                os.system('./processing.sh {} {} {}'.format(names[i], k+1, nfiles[i]))

os.system('./statistics.sh')
