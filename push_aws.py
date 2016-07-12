import boto
import sys
import os
import argparse




def add_op(bucketName, folderName, fileName):
    s3 = boto.connect_s3()
    print "Creating/accessing bucket..."
    bucket = s3.get_bucket(bucketName)
    if bucket == None:
        bucket = s3.create_bucket(bucketName)
        
    print "Creating key bind to folder/file..."
    key = bucket.get_key(folderName + '/' + fileName)
    if key == None:
        key = bucket.new_key(folderName + '/' + fileName)
    
    print 'Sending file upstream...'
    key.set_contents_from_filename('./' + fileName)
    key.set_acl('public-read')



def rm_op(bucketName, folderName, fileName):
    s3 = boto.connect_s3()
    print "Getting bucket name..."
    bucket = s3.get_bucket(bucketName)
    print "Retrieving file..."
    key = bucket.get_key(folderName + '/' + fileName)
    if key == None:
        print 'Can\'t delete a file that isn\'t stored on the server.'
    else:
        print "Deleting file..."
        bucket.delete_key(key)
        



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

if args.op == 'A' or args.op == 'a':
    add_op(args.bu, args.fo, args.fi)
elif args.op == 'R' or args.op =='r':
    rm_op(args.bu, args.fo, args.fi)
    

