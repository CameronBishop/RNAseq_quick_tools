# usage give_fasta_seq_lengths.py <fasta.fa> <output.txt>

import sys
import re

headers = []
lengths = []
nucleotides = ('.*[acgtACGT]$')

output = open(sys.argv[2], "w+")

with open(sys.argv[1]) as fastin:
    for line in fastin:
        if line.startswith(">"):
            headers.append(line.strip('\n'))
        elif re.match(nucleotides, line):
            lengths.append(len(line.strip('\n')))

if len(headers) == len(lengths):
    output.write('Locus\tLength\n')
    for i in headers:
        output.write(headers[headers.index(i)] + '\t' + str(lengths[headers.index(i)]) + '\n')
else:
    print('Error: list are of unequal length')

fastin.close()
