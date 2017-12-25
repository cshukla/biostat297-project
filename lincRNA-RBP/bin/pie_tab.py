#!/usr/bin/env python
from optparse import OptionParser
import os
import numpy as np
import scipy as sp

###################################################################################
# pie_tab.py
#
# For each motif, output a tab delimited file corresponding to the number of cds,
# lncrna, pseudogene, 3' utrs, 5' utrs, rrna and small rna hits. The output of the
# file needs to be used as an input to generate a heatmap.
###################################################################################

################################################################################
# main
################################################################################
def main():
    elements = ['cds', 'pseudogene', 'lncrna', 'rrna', 'smallrna', 'utrs_3p', 'utrs_5p']
    motif_out ={}
    usage = 'usage: %prog [options] <bed_file> <gff_file>'
    parser = OptionParser(usage)
    #parser.add_option()
    (options,args)=parser.parse_args()
    
    if len(args) != 2:
        parser.error('Must provide both bed results file and gff file')
    else:
        bed_file = args[0]
        gff_file = args[1]
    
    for line in open(gff_file):
        temp = line.split()
        motif_id = temp[8]
        if motif_id not in motif_out:
            motif_out[motif_id] = 1
        
    all_motifs = sorted(motif_out.keys())

    raw_path = bed_file.split('/')
    iter1 = 0
    paths = {}
    for i in range(0,len(elements)):
        for j in range (0,len(all_motifs)):
            add_path = [elements[i], all_motifs[j]]
            path = raw_path + add_path
            paths[iter1] = '/'.join(path)
            iter1 = iter1+1

    pie_values = {}
    for i in range(0,len(paths)):
        if os.path.isfile(paths[i]) == 1:
            file = open(paths[i])
            file = file.read()
            file = file.strip()
            lines = file.split('\n')
            pie_values[i] = len(lines)
        else:
            pie_values[i] = 0

    TableOfValues = {}
    iter = 0
    for i in range(0,len(elements)):
        MyList = []
        count = 0
        for j in range(0,(len(paths)/len(elements))):
            MyListIndex = i + count + iter
            MyList.append(pie_values[MyListIndex])
            TableOfValues[elements[i]] = MyList
            count = count+1

        iter = iter + len(all_motifs) - 1

    for key, value in TableOfValues:
        print '\t'.join((key, (value))
"""
    RowDict = {}
    for i in range(0,len(all_motifs)):
        temp = []
        k = 0
        for j in range(0,(len(paths)/len(all_motifs))):
            temp.append(pie_values[k+i])
            RowDict[all_motifs[i]] = temp
            k = k+len(all_motifs)


    aRowTotals = []
    for i in range(0,len(all_motifs)):
        aRowTotals.append(sum(RowDict[all_motifs[i]]))

    LogValues = [-1.05929543, -2.26915032, -1.95404313, -7.60090246, -4.54690128,
              -1.17182835, -2.44299725]
    for i in range(0,len(all_motifs)):
        for j in range(0,len(elements)):
            if TableOfValues[elements[j]][i] !=0:
                TableOfValues[elements[j]][i] = (np.log(TableOfValues[elements[j]][i]/float(aRowTotals[i]))) - LogValues[j]
            else:
                TableOfValues[elements[j]][i] = -2

    motif_names = []
    for i in range(0, len(all_motifs)):
        temp = all_motifs[i]
        temp = temp.split('_')
        motif_names.append(temp[0])
"""

################################################################################
# __main__
################################################################################
if __name__ == '__main__':
    main()
