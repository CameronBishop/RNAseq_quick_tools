# usage: fastq_to_fasta_and_remove_wrap.py input.fa output.fa header_prefix

# note: In order for python to know which lines are headers, the user must specify a 'header_iq'
# this should be a string common to every header, and be at the beginning of the line
# simply specifying '@ is not satisfactory, as '@' also occurs in phred scores.

# header example:
# @locus_tag_*******
# in which case the header prefix would be '@locus_tag_'

import sys
import re
fasta = open(sys.argv[2], 'w+')

#store all non-fastq lines in an array
getlines = False
array = []
plus = ('\+$')
with open(sys.argv[1]) as fastqin:
     for line in fastqin:
        if line.startswith(sys.argv[3]):
            getlines = True
        if re.match(plus, line):
            getlines = False
        if getlines:
            array.append(line.strip("\n"))

#loop through the array and, for each locus, join sequence elements into a single string (remove wrapping)
temp = []
for i in array:
    if i.startswith("@"):
        temp = [] # if data exist in temp, delete it
        fasta.write(i.replace('@', '>') + "\n")
    if not i.startswith("@"):
        temp.append(i.strip()) #join seq elements into on string
        if array.index(i) == (len(array) - 1):  #if element is the last one, print the joined elements
            fasta.write("".join(temp) + "\n")
        elif array[array.index(i) + 1].startswith("@"): #if element preceeds a header, print the joined elements
            fasta.write("".join(temp) + "\n")
