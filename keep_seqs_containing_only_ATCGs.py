# usage: keep_seqs_containing_only_ATCGs.py input.fa output.fa

# script reads a multifasta file. reads lines that don't start with ">".
# if a line has any non ATCG characters, that line (the sequence) and the line above (the header) are excluded from the output.

import sys
import re

allowed = re.compile("^[atcgATCG]+$")

if len(sys.argv) == 3:
    fastout = open(sys.argv[2], "w+")
    with open(sys.argv[1]) as fastin:
        for line in fastin:
            if line.startswith(">"):
                header = line
            if not line.startswith(">"):
                if allowed.match(line):
                    fastout.write(header)
                    fastout.write(line)
    fastin.close()
else:
    print('Error: Wrong number of arguments')
