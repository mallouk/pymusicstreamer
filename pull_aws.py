import boto
import sys
import os
import argparse

def splitRecursiveDirs(entry):
    numSlashes = entry.count('/')
    if numSlashes > 1:
        parsedEntry = entry.split('/')
        dots = '.' * (numSlashes - 1)*3
        print dots + parsedEntry[numSlashes-1] + '/'
    else:
        print entry


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

parser.add_argument('-fo', action='store', help='folder name to filter on')
parser.add_argument('-dirs', action='store_true', help='only pull back the directory names')
parser.add_argument('-bu', action='store', default='musictestapp', help='bucket name to create')


args = parser.parse_args()

s3 = boto.connect_s3()
bucket = s3.get_bucket(args.bu)
key = bucket.get_all_keys()

if args.fo == defaultArg:
    args.fo = ''

filesList = bucket.list(args.fo)
for files in filesList:
    entry = files.name
    if entry.endswith('/'):
        splitRecursiveDirs(entry)
    else:
        if args.dirs != True:
            parsedEntry = entry.split('/', 1)
            splitRecursive(parsedEntry, len(parsedEntry), 1)
