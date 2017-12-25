import sys, scipy.stats

"""
This python script tests the significnce of each indivdual seed match (within a given miRNA 
	family) to the lincRNA background using a t-test and assuming pooled variance of the seed and the 
	background combined. The output is a list of the t-statistic and the one-tailed pvalue ordered 
	because the command line argument is
	>>python ttest.py miR-22-1.txt |sort -grk2 > pvals.out

	for any miRNA family of interest.
"""
mfn = sys.argv[1]
ref = 'lncrna.txt'

x = [float(line.rstrip()) for line in open(ref)]

def get_mrna(mfn):
    y = []
    for line in open(mfn):
        line = float(line.rstrip())
        y.append(line)
        if len(y) > 0 and len(y)%7 == 0:
            yield y[-7:]


for mrna in get_mrna(mfn):
    [t,pval] = scipy.stats.ttest_ind(x, mrna)
    print t, pval/2.
