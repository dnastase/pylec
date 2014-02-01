#!/usr/bin/env python3

import sys, optparse

for f in sys.argv[2:]:
   for line in open(f):
      if sys.argv[1] in line:
         found = True
         break
   else:
      found = False
   if not found:
      continue
   print("File %s has '%s'" % (f, sys.argv[1]))

