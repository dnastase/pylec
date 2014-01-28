#!/usr/bin/env python3

import sys

string = sys.argv[1]
inputFile = sys.argv[2]

for line in open(inputFile):
   if string in line:
      print(line, end='')
