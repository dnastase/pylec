#!/usr/bin/env python3

n=2
f=3.14
s="string"
n1 = n + 1
s1 = "another" + s

print(n, f s)

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

#removing
del l[3:5]
l

for e in l: print e

def fun():
   pass


if condition1:
   body1
elif condition2:
   body2
else:
   bodyN
 
if n > 2: print ">2" 
elif n < 2: print "<2"
else: print "=2"

