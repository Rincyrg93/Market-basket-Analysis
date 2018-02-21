#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 11:19:52 2018

@author: rincygeorge
"""

import pandas as pd
import csv

df=pd.read_csv('/Users/rincygeorge/Desktop/basketNew.csv')
   
for col in df.columns:
    df[col]=df[col].map(lambda x:col if x==' true' else ' false')
temp1=[]
temp2=[]
for r1 in df.iterrows():
    index,data=r1
    temp1.append(data.tolist())
o=[[y for y in x if y!=' false'] for x in temp1]
str1=[','.join(x for x in y) for y in o]

f=open('/Users/rincygeorge/Desktop/basket.csv','w')
w=csv.writer(f, delimiter=',')
w.writerows([x.split(',') for x in str1])
f.close()
