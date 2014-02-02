#!/usr/bin/env python3

n=2
f=3.14
s="string"
n1 = n + 1
s1 = "another" + s

print(n, f s)

if n > 2: print ">2" 
elif n < 2: print "<2"
else: print "=2"


# creating
l = [2, 3.14, "py", n, f, s]
l2 = list("abc")

#accessing
l[1]
l[1:3]
l[-1]
l[2:]
l[:]

#adding
l.append("new")
l    
l.insert(1, 44)
l
l[1:1] = 55
l

del l[1]
l
l.pop(1)
l
l.remove("new")
l

l=[7, 6, 8, 3.14]
l[0:2]=[3, 1, 2]
l
l.sort()
l

del l[3:5]
l
for e in l: print e

done = False
while not done:
    cmd = raw_input("new command:")
    if 'exit' in cmd:
        done = True
    elif 'show' in cmd:
        DoShow()
    elif 'assign' in cmd:
        DoAssign()


d={'john': 12, 'mary': 34, 'brad':56}
d
d=dict(john=12, mary=34, brad=56)
d

d['ana']=78
d
d.update({'steve':90})
d

del d['ana']
d
d.pop('steve')
d

'mary' in d


for key in d.key():
   pass

for val in d.values():
   pass

for (key, val) in d.items()
   pass


def mysum(l):
    theSum = reduce(lambda x,y: x+y, l)   
    return theSum


import numpy
m = numpy.median(l)

from numpy import median
m = median(l)



import rpy2.robjects as robj
>>> pi = robjects.r['pi']
>>> pi[0]
3.14159265358979
robjects.r('''
        f <- function(r, verbose=FALSE) {
            if (verbose) {
                cat("I am calling f().\n")
            }
            2 * pi * r
        }
        f(3)
        ''')
>>> letters = robjects.r['letters']
>>> rcode = 'paste(%s, collapse="-")' %(letters.r_repr())
>>> res = robjects.r(rcode)
>>> print(res)
"a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z"
