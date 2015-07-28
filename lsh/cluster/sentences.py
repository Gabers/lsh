'''
Created on Apr 19, 2015

@author: gabrielryan
'''

def similarPairs(lengthDict, bucketDict, distanceMeas, options=None):
    # parse options
    if (options is None):
        options = {}
    verbose = False
    if ('verbose' in options):
        verbose = options['verbose']

    pairs = 0
    comparisons = 0
#     pairList = []
    for length in lengthDict.keys():
        if (verbose):
          print "comparing length " + str(length) + " found " + str(pairs) + " with " + str(comparisons) + " comparisons"
        for sentence in lengthDict[length]:
            #check for pairs at same length
            pairedSentencesList = []
            for i in range(2):
                if (i >= length):
                    break
                else:
                    for j in range(2):
                        key = hash((sentence[i],length+j))
                        if key in bucketDict:
                            bucket = bucketDict[key]
                            for bucketSentence in bucket:
                                if (bucketSentence is sentence) or (bucketSentence in pairedSentencesList):
                                    pass
                                else:
                                    comparisons = comparisons + 1
#                                     print "comparing: "+str(bucketSentence)+" "+str(sentence)+" "+\
#                                           str(distanceMeas(bucketSentence,sentence))
                                    if (distanceMeas(bucketSentence, sentence,1) <= 1):
#                                         print " added"
                                        pairs = pairs + 1
                                        pairedSentencesList.append(bucketSentence)

        
                            
    return pairs
