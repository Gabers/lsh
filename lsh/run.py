'''
Created on Apr 17, 2015

@author: gabrielryan
'''

import cluster.sentences
import cluster.dist
import sys


def runOnFile(inputFile, options=None):
    # first parse options
    if options is None:
        options = {}

    maxLines = sys.maxint
    verbose = False
    useHash = True
    if 'maxLines' in options:
        maxLines = options['maxLines']
    if 'verbose' in options:
        verbose = options['verbose']
    if 'useHash' in options:
        useHash = options['useHash']
    
    # dict hashing sentences to lengths + vals
    #  keys = length of sentences in bucket
    #  vals = list of sentences
    bucketDict = {}
    lengthDict = {}
    
    buckets = 0
    
    if verbose:
        print "parsing " + inputFile
    # loop thru file, store sentences indexed by len & 2 first words
    with open(inputFile,"r") as infile:
        numRead = 0
        for line in infile:
            numRead = numRead + 1
            if (numRead > maxLines):
                break
            lineList = line.split()[1:]
            if (useHash):
              wordHashList = map(hash,lineList)
            else:
              wordHashList = lineList
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

    if (verbose):
      print str(numRead) + " lines read into " + str(buckets) + " buckets"
      print "counting pairs"

    pairs = cluster.sentences.similarPairs(lengthDict, bucketDict, cluster.dist.editDist)
    
    if (verbose):
      print str(pairs) + " pairs counted "# + str(comparisons) + " comparisons"

    return pairs

