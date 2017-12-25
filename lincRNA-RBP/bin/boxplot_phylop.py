#!/usr/bin/env python

from optparse import OptionParser
import numpy
import glob
import sys
import matplotlib.pyplot as py
import random

##############################################################################
# boxplot_phylop.py
# 
# This script outputs box plots for each motif file versus the background file
#
##############################################################################
def main():
	usage = 'usage: %prog [options] <motif_files_folder>'
	parser = OptionParser(usage)
	if len(sys.argv) != 2:
		raise Exception ("Please provide the folder with the motif files and background values file")

	motif_files = glob.glob(sys.argv[1] + 'M*.txt')
	motifs = []
	for i in range(0,len(motif_files)):
		temp = motif_files[i].split('/')[-1]
		motifs.append(temp.split('_')[0])
		
	background_values = []
	i = 0
	for line in open(sys.argv[1] + 'intron.txt','r'):
		i += 1

	prob = 10,000/i
	for line in open(sys.argv[1] + 'intron.txt', 'r'):
		if random.random()< prob:
			background_values.append(float(line))

	motif_values = {}
	for i in range(0,len(motif_files)):
		motif_values[motifs[i]] = []

	for i in range(0,len(motif_files)):
		for line in open(motif_files[i],'r'):
			if random.random()<0.1:
				motif_values[motifs[i]].append(float(line))
	
	motif_values['background'] = background_values
	plots_file = []
	for i in range(0,len(motifs)):
		plots_file.append(sys.argv[1] + 'boxplots/' + motifs[i] + '.png')

	
	data = motif_values.values()
	py.figure()
	py.boxplot(data)
	py.savefig(sys.argv[1] + 'all_motifs.png', dpi=200)
	py.close()

###########################################################################
#
###########################################################################
if __name__ == '__main__':
	main()