# usage ncbi_cds_only_locustag_in_headers.py <cds_in.fa> <cds_out.fa>

# For each CDS, the script creates a new header consisting of only the locus tag for headers, instead of all the many many space-delimited fields included in the NCBI file.
# The input fasta file must have 'wrapping' removed first.

import re
import sys

if len(sys.argv) == 3:
    cdsout = open(sys.argv[2], "w+")
    with open(sys.argv[1]) as cdsin:
        cds_array = cdsin.readlines()   # read the fasta file into an array
        for i in cds_array:             # loop over the array, and process the headers
            if i.startswith(">"):
                header = i.rstrip('\n')
                tag = re.findall('locus_tag=\w+', header)   # store the locus_tag, convert to string, and create a new header
                tag = (str(tag[0]))
                header = ">" + tag
                place = cds_array.index(i)                  # store the current index, and use to store the corresponding seq
                seq = cds_array[place + 1].strip("\n")
                cdsout.write(header + "\n")
                cdsout.write(seq + "\n")                    # write the output file
    cdsin.close()
else:
    print('Error: Wrong number of arguments')
