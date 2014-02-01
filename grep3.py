#!/usr/bin/env python3

import sys, optparse

def LOG(text):
   print(text, file=sys.stderr)


def grep(string, inputFile, ignoreCase=False):
   for line in open(inputFile).readlines():
      line = line.rstrip("\n")

      if not ignoreCase and string in line:
         print(line) 
         LOG("matched with case %s in line %s" % (string, line))
      elif ignoreCase and string.lower() in line.lower():
         print(line) 
         LOG("matched w/out case %s in line %s" % (string, line))
      else:
         LOG("no match for %s in line %s" % (string, line))
    
cmdLineParser = optparse.OptionParser()
#cmdLineParser.add_option("-n", action="store", type="int", dest="ndays", default = 0, help="Number of days to process")
#cmdLineParser.add_option("-d", action="store", type="string", dest="date", default=datetime.datetime.today().strftime("%Y%m%d"), help="(YYMMDD) The date for which you want the stats. Default is today")
cmdLineParser.add_option("-i", action="store_true", dest="ignore_case", default = False, help = "ignore case")

#parse the command line arguments
(options, args) = cmdLineParser.parse_args(sys.argv)

string = args[1]      #this is the string to search for
inputFile = args[2]   #this is the file to search into

grep(string, inputFile, options.ignore_case)

