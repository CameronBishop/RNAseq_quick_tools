# usage: python extract_in-frame_CDSs_from_fasta.py input.fa output.fa

# note: use something like 'grep -E -B 1 '^ATG|^GTG|^TTG|' Aag2_shared.fa | grep -E -B 1 'TAG$|TGA$|TAA$' | grep -v "^--$" > Aag2_shared_correct_codons.fa'
# to first ensure correct start/stop codons are present before running this script.

import sys
import re

headers = []
seqs = []
nucleotides = ('.*[AaCcTtGg]$')

if len(sys.argv) == 3:
    outfast = open(sys.argv[2], "w+")

    # store headers and sequences in seqarate lists
    with open(sys.argv[1]) as fastin:
        for line in fastin:
            if line.startswith(">"):
                headers.append(line.strip('\n'))
            elif re.match(nucleotides, line):
                seqs.append(line.strip('\n'))

    # loop through the seqs list and add in-frame seqs and respective headers to the ouput file.
    if not len(headers) == len(seqs):
        print('Error: Problem with fasta file', '\n', 'Number of header lines does not equal number of sequence lines')
    elif len(headers) == len(seqs):
        for i, val in enumerate(seqs):
            if len(val)%3 == 0:
                outfast.write(headers[i] + '\n')
                outfast.write(seqs[i] + '\n')
        print('Job completed. Output saved in:', sys.argv[2])

    fastin.close()
else:
    print('Error: Wrong number of arguments')
