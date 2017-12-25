"""
This program will find all non-overlapping perfect seed matches between miRNAs and lincRNAs.  This code finds
multiple hits within a given lincRNA as well. Specifically, this file takes two files as input:

- The first file is a tab-delimited parsed version of the lincRNA transcriptome.  For each row in this file, column 1
corresponds to the carrot symbol (I kept this in to help interconversions), column 2 corresponds to each lincRNA's ensemble I.D.,
column 3 contains the chromosome number (+ and - have been omitted), column 4 contains the genomic coordinates for each
exon of the lincRNA, and column 5 contains each lincRNA's sequence.  To generate this file, the lincRNA transcriptome
was parsed such that all information for a given lincRNA was combined on one line.  Then, the above columns were created in excel 
by converting spaces in each row to tabs.  

- The second file is a tab-delimited file.  Column 1 contains the miRNA family name, and Column 2 contains the miRNA family seed
sequence.

The resulting output file is in BED format.  It has 4 tab-delimited columns where column 1 corresponds to the chromosomal location
of a given seed match, column 2 is the starting chromosomal position, column 3 is the ending chromosomal position, and column 4 is
the corresponding miRNA family that has a seed present at the genomic location.

Usage:  python Target2Pretty.py Parsed_TabDelimited_Transcriptome_file miRNAFamily_miRNASeed_file
"""
import sys
import re

with open(sys.argv[2]) as file2:
	tat = "\t".join(["chr", "start","end","miRNA"])
	for eachline in file2:
		eline = eachline.strip().split("\t")
		miRNA_Family, miRNA_Seed = eline
		with open(sys.argv[1]) as file:
			for strLine in file:
				astrLine = strLine.strip( ).split( "\t" )
				carrot, ensemble, chromosome, start_end, seq = astrLine
				r = re.compile(r'{0}'.format(miRNA_Seed))
				#Since we are going to search for the miRNA_Seed in the transcriptome many times, re.compile makes doing so 
				#more efficiently
				for match in r.finditer(seq):
				#This command finds the nucleotide index of each non-overlapping seed match in a lincRNA nucleotide sequence
					mtch_starting_index = int(match.start(0)) 
					mtch_ending_index = int(match.end(0)) 
					pos = re.findall(r'(\d+-\d+)',start_end)
					#This command captures the genomic locations of each lincRNA exon if a given miRNA seed matched the sequence
					for i in range(len(pos)):
						e = pos[i].strip().split("-")
						exon_start,exon_end = e
						#exon_start and exon_end represent the start and stop position of each lincRNA exon
						if (int(exon_start) + int(mtch_starting_index)) <= int(exon_end):
							if (int(mtch_ending_index) <= int(exon_end)):
								#The double if loop prevents matches across different exons
								start = int(exon_start) + int(mtch_starting_index)
								end = int(exon_start) + (int(mtch_ending_index) - 1) 
								#This command gives the exact genomic coordinates of the seed match.  The inclusion of a "-1" is necessary
								#in order to account for the fact that python begins counting at "0" instead of "1".
								d = "\t".join([chromosome,str(start),str(end),miRNA_Family])
								tat = "\n".join([tat,d])
							break
							#This prevents the code from analyzing every exon after it finds the correct one.  This is part of the new correct code.
						else:
							mtch_starting_index = int(mtch_starting_index) - ((int(exon_end) - int(exon_start)) + 1)
							mtch_ending_index = int(mtch_ending_index) - ((int(exon_end) - int(exon_start)) + 1)
							#If a given seed match is not in an exon,the above two commands update the start and end index of the seed match.  This is necessary in order to account for the
							#change in nucleotide index when looking at the next lincRNA exon.  This is part of the new correct code.
print(tat)
