#!/usr/bin/env python
from optparse import OptionParser
import os

###################################################################################
# motif_split.py
#
# Take intersectBed file as input and split into multiple files; one file for each
# motif.
###################################################################################

################################################################################
# main
################################################################################
def main():
    motif_out ={}
    usage = 'usage: %prog [options] <bed_file>'
    parser = OptionParser(usage)
    #parser.add_option()
    (options,args)=parser.parse_args()
    
    if len(args) != 1:
        parser.error('Must provide bed results file')
    else:
        bed_file = args[0]
    
    for line in open(bed_file):
        a = line.strip().split()
        motif_id = a[8]
        path = bed_file.split('/')
        path[-1] = motif_id
        path = '/'.join(path)
        if motif_id not in motif_out:
            motif_out[motif_id] = open(path,'w')
        
        print >> motif_out[motif_id], line,

################################################################################
# __main__
################################################################################
if __name__ == '__main__':
    main()