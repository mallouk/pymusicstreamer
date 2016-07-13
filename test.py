import os
import boto
import sys
import argparse

defaultArg = 'NO_ARG_PASSED'
parser = argparse.ArgumentParser(argument_default=defaultArg);

parser.add_argument('-fo', action='store', help='folder name to create')
parser.add_argument('-fi', action='store', help='file name to create')
parser.add_argument('-bu', action='store', default='musictestapp', help='bucket name to create')
parser.add_argument('-op', action='store', required=True, help='code to determine if we add/remove params:(A/R)')

args = parser.parse_args()

if args.fo == 'NO_ARG_PASSED' and args.fi == 'NO_ARG_PASSED':
    print "Error. You need to give a folder and/or file name as a param"
    print '  -h, --help  show a help message and exit'
    print '  -fo FO      folder name to create'
    print '  -fi FI      file name to create'
    print '  -bu BU      bucket name to create'
    print '  -op OP      code to determine if we add/remove params:(A/R)'
    exit()

