"""
The code that follows will take a miRNA seed (or any RNA sequence for that matter) and convert it into the corresponding DNA inverse complement.
This code takes as input a file containing two tab-delimited columns without a header.  The first column consists of the miRNA family identifiers.  The second
column contains the miRNA sequence corresponding to the miRNA families.

The resulting output file is in the same format as the input file, except the sequence in column 2 is now the inverse complement.

Usage:  python miRNA_REverseComplement.py miRNA_FamiliesandSequences.txt > output.txt
"""


import sys
import re
import csv


def revComplement(seq):
	basecomplement = {'A':'T','C':'G','G':'C','U':'A'}
	#The above command creates a dictionary that can be used to find the complement of the RNA
	letters = list(seq)
	letters.reverse()
	#This reverses/inverses the RNA sequence provided
	dna = ''
	for base in letters:
		dna += basecomplement[base]
	return dna

a = "\t".join(["miRNA Family", "Inverse Complement"])
b = []

with open(sys.argv[1]) as f:
	for strLine in f:
		astrLine = strLine.strip( ).split( "\t" )
		miRNA_Family, sequence = astrLine
		strRevcomp = revComplement(sequence)
		d = "\t".join([miRNA_Family,strRevcomp])
		a = "\n".join([a,d])
		
print(a)
	