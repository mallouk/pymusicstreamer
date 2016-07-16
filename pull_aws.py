import boto
import sys
import os
import argparse

def splitRecursive(parsedEntry, arrayLen, execLevel):
    for i in range(arrayLen - (arrayLen - 1), arrayLen):
        parse = parsedEntry[i].split('/')
        if len(parse) > 1:
            execLevel = execLevel + 1
            splitRecursive(parse, len(parse), execLevel)
        else:
            dots = '.' * (execLevel * 3)
            print dots + parsedEntry[i]

defaultArg = 'NO_ARG_PASSED'
parser = argparse.ArgumentParser(argument_default=defaultArg);

parser.add_argument('-fo', action='store', help='folder name to create')
parser.add_argument('-fi', action='store', help='file name to create')
parser.add_argument('-bu', action='store', default='musictestapp', help='bucket name to create')
parser.add_argument('-op', action='store', help='code to determine if we add/remove params:(A/R)')

args = parser.parse_args()



s3 = boto.connect_s3()
bucket = s3.get_bucket(args.bu)
key = bucket.get_all_keys()

filesList = bucket.list()
for files in filesList:
    entry = files.name
    if entry.endswith('/'):
        print entry
    else:
        parsedEntry = entry.split('/', 1)
        splitRecursive(parsedEntry, len(parsedEntry), 1)
    
