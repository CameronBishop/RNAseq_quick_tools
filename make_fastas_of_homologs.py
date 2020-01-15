#usage: make_fastas_of_homologs list_of_filenames.txt

# The script requires a number of multi-fasta files, with their /location/filename listed in a txt file. the txt filename should be given as an argument.
# The script will then make a list of headers based on the contents of the first fasta file named in the txt file. Using this list it will search for
# homologous sequences and create a multifasta file for each homologue, with headers indicating the origin of each sequence.

import sys
import os

wdfiles = []
headers = []

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

    # make a list of headers based on the contents of the first file named in txtnames
    with open(txtnames[0]) as read1:
        for line in read1:
            if line.startswith('>'):
                headers.append(line.strip('\n'))

    # loop through header list. for each element, open each file listed in txtnames
    for i in headers:
        writing = []
        outname = i.replace('>', '') + '.fa'
        fastout = open(outname, 'w+')
        for j in txtnames:
            with open(j) as fastin:
                for line in fastin:

                    # extract the header and seq associated with i, and generate a multifasta
                    if line.strip() == i:
                        writing.append(line.strip() + '_in_' + j + '\n')
                        writing.append(next(fastin))
        for k in writing:
            fastout.write(k)
