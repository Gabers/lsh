from nose.tools import *
import lsh.run

def setup():
    print "setup"

def teardown():
    print "teardown"

def basic_test():
    options = { 'useHash' : False,
                'verbose' : True }
    pairs = lsh.run.runOnFile('data/sentence_sample.txt', options)
    assert pairs == 2
