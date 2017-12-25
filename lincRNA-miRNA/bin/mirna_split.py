#!/usr/bin/env python
from optparse import OptionParser
import os

###################################################################################
# motif_split.py
#
# Take file with all mirna hits as input and split into multiple files; one file 
# for each miRNA family.
###################################################################################

################################################################################
# main
################################################################################
def main():
    mirna ={}
    usage = 'usage: %prog [options] <mirna_all_families>'
    parser = OptionParser(usage)
    #parser.add_option()
    (options,args)=parser.parse_args()
    
    if len(args) != 1:
        parser.error('Must provide mirna_all_families file')
    else:
        mirna_all_families = args[0]
    
    for line in open(mirna_all_families):
        a = line.strip().split()
        mirna_family = a[3]
        a[3] = '\n'
        path = mirna_all_families.split('/')
        path[-1] = mirna_family +'.txt'
        path = '/'.join(path)
        if mirna_family not in mirna:
            mirna[mirna_family] = open(path,'w')
        
        print >> mirna[mirna_family], '\t'.join(a[0:4]),

################################################################################
# __main__
################################################################################
if __name__ == '__main__':
    main()