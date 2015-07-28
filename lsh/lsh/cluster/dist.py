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
        maxDistExceeded = True
        for j in range(1,table.shape[1]):
#             print str(wi[i-1])+" "+str(wj[j-1])
            sub = 1
            if (wi[i-1] == wj[j-1]):
                sub = 0
            table[i,j] = min(table[i,j-1]+1,
                             table[i-1,j]+1,
                             table[i-1,j-1]+sub)
            if(table[i,j] <= maxDist):
                maxDistExceeded = False
        # speed up comparison if we're only checking for a threshold
        if maxDistExceeded:
            return maxDist + 1
        
    return table[-1,-1]
