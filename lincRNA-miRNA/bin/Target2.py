import sys
import re

with open(sys.argv[2]) as file2:
	tat = "\t".join(["chr", "start","end","miRNA"])
	for eachline in file2:
		eline = eachline.strip().split("\t")
		miRNA_Family, miRNA = eline
		with open(sys.argv[1]) as file:
			for strLine in file:
				astrLine = strLine.strip( ).split( "\t" )
				lnc, ensemble, chr, start_end, seq = astrLine
				r = re.compile(r'{0}'.format(miRNA))
				for match in r.finditer(seq):
					ut = int(match.start(0))
					tu = int(match.end(0))
					pos = re.findall(r'(\d+-\d+)',start_end)
					for i in range(len(pos)):
						e = pos[i].strip().split("-")
						t,y = e
						if (int(t) + int(ut)) <= int(y):
							start = int(t) + int(ut)
							end = int(t) + (int(tu) - 1)
							d = "\t".join([chr,str(start),str(end),miRNA_Family])
							tat = "\n".join([tat,d])
						else:
							break
			
				#e = "\t".join([mir,set,etc,some,seq[c]])
		#for match in re.finditer(r'AC',seq):
			#print match.span()
print(tat)