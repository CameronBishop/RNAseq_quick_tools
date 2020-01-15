# usage: keep_homologs_with_variation.py fasta_list.txt

# For each multi-fasta file, if at least one sequence in the file is unique, that fasta's filename is added to a list and saved in the WD as 'variable_homologs.txt'

import sys
import os
import re

wdfiles = []
headers = []
usefulloci = []

# store all filenames in wd in a list
for root, dirs, files in os.walk("."):
    for name in files:
        wdfiles.append(name.strip('\n'))

# store all filenames in the txt file in a list
with open(sys.argv[1]) as txt:
    txtnames = [line.strip('\n') for line in txt]

    # check if all files named in txt are in working dir, before continuing
    if not (set(txtnames).issubset(set(wdfiles))):
        for i in txtnames:
            if not i in wdfiles:
                print('Error: ' + i + ' is missing from the working directory')
    else:
        for i in txtnames:
            with open(i) as fastin:
                for line in fastin:
                    if line.startswith('>'):
                        seq = next(fastin).strip('\n')
                        if line.startswith('>'):
                            break
                    break

            with open(i) as fastin2:
                checker = []
                for line2 in fastin2:
                    if not line2.startswith('>'):
                        if line2.strip() == seq:
                            checker.append(0)
                        else:
                            checker.append(1)
                if 1 in checker:
                    usefulloci.append(i)

fileout = open('variable_homologs.txt', 'w+')
for locus in usefulloci:
    fileout.write(locus + '\n')
