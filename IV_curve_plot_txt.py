# -*- coding: utf-8 -*-
"""
This program can be used to plot I-V curve in .txt format file
@author AnnengYang/9-3-2017
"""

import matplotlib.pyplot as plt
import matplotlib.axes as axes
import os
import numpy as np
#open file 
def plot(file):
    with open(file, 'r') as f:
        f=f.read()
    f=f.replace(' ', '').replace(',,,',',')
    data_txt=[i for i in f.split('\n')]
    column=data_txt[data_txt.index('#DATA')+2]
#transfer file to 2D list   
    column=column.split(',')
    column=column[:-1]
    data_fulltxt=data_txt[data_txt.index('#DATA')+3:]
    data_full=[[digit for digit in line.split(',')] for line in data_fulltxt]
    [row.pop() for row in data_full]
    data_full.pop()
#add None to the empty element and  short row elements at bottom few rows   
    for i in range(len(data_full)):
        if len(data_full[i])<len(data_full[i-1]):
            length=len(data_full[i-1])-len(data_full[i])
            for e in range(length):
                data_full[i].append(None)
    for row in data_full:
        for i in range(len(row)):
            if row[i]=='':
                row[i]=None
#transfer list to array and plot single file in a figure    
    data=np.array(data_full).transpose()            
    plt.figure(figsize=(8,6))
    for i in range(0,len(column),3):
        plt.plot(data[i],data[i+2],'ro',markersize=3, linewidth=1.2)
        plt.xlabel('VG/V')
        plt.ylabel('ID/A') 
    plt.ticklabel_format(axis='y',style='sci',scilimits=(1,4))
    # plt.gca().invert_yaxis()    #invert y axis
    plt.tight_layout()
    plt.savefig('%s.png' %file.strip('.txt'), dpi=600)
    print('%s.png has been saved' %file.strip('.txt'))
    
dir_path = os.path.dirname(os.path.realpath(__file__))
files=[]

for file in os.listdir(dir_path):
    if file.endswith(".txt"):
        files.append(file)
        print(os.path.join(dir_path, file))
        
for file in files:
    plot(file)

