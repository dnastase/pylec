#!/usr/bin/env python3

import sys, optparse

def LOG(text):
   print(text, file=sys.stderr)

cmdLineParser = optparse.OptionParser()
#cmdLineParser.add_option("-n", action="store", type="int", dest="ndays", default = 0, help="Number of days to process")
#cmdLineParser.add_option("-d", action="store", type="string", dest="date", default=datetime.datetime.today().strftime("%Y%m%d"), help="(YYMMDD) The date for which you want the stats. Default is today")
cmdLineParser.add_option("-i", action="store_true", dest="ignore_case", default = False, help = "ignore case")

(options, args) = cmdLineParser.parse_args(sys.argv)

string = args[1]
inputFile = args[2]

for line in open(inputFile).readlines():
   line = line.rstrip("\n")

   if not options.ignore_case and string in line:
      print(line) 
      LOG("matched with case %s in line %s" % (string, line))
   elif options.ignore_case and string.lower() in line.lower():
      print(line) 
      LOG("matched case insensitive %s in line %s" % (string, line))
   else:
      LOG("not match for %s in line %s" % (string, line))

