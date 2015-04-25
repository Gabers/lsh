'''
Created on Apr 17, 2015

@author: gabrielryan
'''

import cluster.sentences
import cluster.dist
import sys, getopt
# import objgraph
# from guppy import hpy




            
            
    


def main():
    print "testing main"
    
    inputFile = "data/sentence_sample.txt"
    if (len(sys.argv) == 2):
        inputFile = sys.argv[1]
    
#     hp = hpy()
    
    # dict hashing sentences to lengths + vals
    #  keys = length of sentences in bucket
    #  vals = list of sentences
    bucketDict = {}
    lengthDict = {}
    
    buckets = 0
    
    print "parsing " + inputFile
    # loop thru file, store sentences indexed by len & 2 first words
    with open(inputFile,"r") as infile:
        numRead = 0
        for line in infile:
            numRead = numRead + 1
            if (numRead > 1000):
                break
            lineList = line.split()[1:]
            wordHashList = lineList
#             wordHashList = map(hash,lineList)
            length = len(wordHashList)
            if (length in lengthDict):
                lengthDict[length].append(wordHashList)
            else:
                lengthDict[length] = [wordHashList]
            for i in range(2):
                if (i >= length):
                    break
                else:
                    key = hash((wordHashList[i],length))
                    if (key in bucketDict):
                        bucketDict[key].append(wordHashList)
                    else:
                        bucketDict[key] = [wordHashList]
                        buckets = buckets + 1

    print str(numRead) + " lines read into " + str(buckets) + " buckets"
    
#     print hp.heap()
    
    
    print "counting pairs"

    pairs = cluster.sentences.similarPairs(lengthDict, bucketDict, cluster.dist.editDist)
    
    #print hp.heap()
#     objgraph.show_most_common_types(limit=20)
                        
    print str(pairs) + " pairs counted "# + str(comparisons) + " comparisons"
#     print pairList


    
    

if __name__ == '__main__':
    main()
    