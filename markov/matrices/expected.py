# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 16:22:11 2018

@author: luciamarock
"""
import sys

dastgah_name=["Segah","RastPanjgah","Nava","Mahour","Homayun","Chahargah","Shur"]
modo = sys.argv[1]
mode=100
for i in range (len(dastgah_name)):
    if modo == dastgah_name[i]:
        mode=i
with open("expected.log", "a") as f:
    f.write(str(mode) + "\n")
    f.close()
