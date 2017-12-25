# Input is the pwm motif file from RNA Compete paper (Tim Hughes)
# Output is a file which serve as an input for PoSSuM

# Input file format (File Name: abcdef.txt)
# Pos A C G U
# i  a1 a2 a3 a4
# j  b1 b2 b3 b4
# k  c1 c2 c3 c4

# Output file format
# BEGIN float
# ID abcdef.txt
# AC abcdef.txt
# DE PoSSuM input file for abcdef.txt
# AL ACGU
# LE k
# MA a1 a2 a3 a4
# MA b1 b2 b3 b4
# MA c1 c2 c3 c4
# END

from __future__ import print_function
outFile = open('PoSSuM_Library.txt','w')
outFile.write('BEGIN GROUP\n')
import glob
files = glob.glob('*.txt')
for i in range(1,len(files)):
    inFile = open(files[i],'r')
    ID = files[i]
    inFile = inFile.read()
    inFile = inFile.strip()
    LE = len(inFile.split('\n'))
    inFile = inFile.split()
    inFile.remove('Pos')
    for j in range (1,LE):
        j =str(j)
        inFile.remove(j)
    Num_Rows = LE - 1
    value_iter = 0
    key_iter = 1
    MA_values = {}
    while key_iter < LE:
        MA_values[key_iter] = inFile[value_iter + 4: value_iter + 8]
        key_iter = key_iter + 1
        value_iter = value_iter + 4
    print('BEGIN FLOAT', file = outFile)
    print('ID %s' %(ID), file = outFile)
    print('AC %s' %(ID), file = outFile)
    print('DE PoSSuM input file for %s' %(ID), file = outFile)
    print('AL ACGU', file = outFile)
    print('LE %s' %(str(Num_Rows)), file = outFile)
    for k in range (1,LE):
        print('MA %s' %(" ".join(MA_values[k])), file = outFile)
    print('END\n', file = outFile)

outFile.write('END')
outFile.close()
