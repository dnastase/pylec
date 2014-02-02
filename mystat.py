#!/usr/bin/env python

""" My statistics module """


PI = 3.1415926

def mysum(l):
    theSum = reduce(lambda x,y: x+y, l)   
    return theSum

if __name__ == "__main__":
   s = mysum([1,2,3])
   print("test: sum: %f" % (s))


