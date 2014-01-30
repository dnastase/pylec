#!/usr/bin/env python3

""" Adds the corresponding values from multiple files (that have the same
structure and number of lines)
"""

import sys, string

inputStream = sys.stdin
if len(sys.argv) > 1:
   inputStream = open(sys.argv[1])

sums = []
lines = inputStream.readlines()
for line in lines:

   items = line.split()

   for (idx, item) in enumerate(items):
      if len(sums) - 1 < idx:
         sums.append(0.)

      t = type(item)

      if t == int:
         sums[idx] += int(item)
      elif t == float:
         sums[idx] += float(item)
      else:
         print("Not a number", item)

for val in sums:
   print(val, ' ', end='')
print()

