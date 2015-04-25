'''
Created on Apr 19, 2015

@author: gabrielryan
'''

import numpy as np


def editDist(wi,wj,maxDist=1000):
    table = np.zeros([len(wi)+1,len(wj)+1])
    table[:,0] = np.arange(table.shape[0])
    table[0,:] = np.arange(table.shape[1])
    for i in range(1,table.shape[0]):
        for j in range(1,table.shape[1]):
            sub = 0
            if (wi[i-1] == wj[j-1]):
                sub = 1
            table[i,j] = min(table[i,j-1]+1,
                             table[i-1,j]+1,
                             table[i-1,j-1]+sub)
    print table
    return table[-1,-1]