# usage: pull_out_fastas.py headers.txt input.fa output.fa

# The script reads a multifasta into an array , then loops over the array. for each element that correspods to a
# header, it searches for a match in a text document of headers. If a match is found, it finds the index of that header in the array.
# Using the index, it appends that element (the matched header) and the next element (the corresponding sequence) to an output file


import sys
import re

if len(sys.argv) == 4:
    fastout = open(sys.argv[3], "w+")

    with open(sys.argv[2]) as fastin:
        fastin_array = fastin.readlines()
        for i in fastin_array:
            if i.startswith(">"):
                header = i.rstrip('\n')

                features = open(sys.argv[1])
                for line in features:
                    temp = line.rstrip('\n')
                    if temp == header:
                        place = fastin_array.index(i)
                        seq = fastin_array[place + 1].strip("\n")
                        fastout.write(header + "\n")
                        fastout.write(seq + "\n")
                features.seek(0)
                features.close()
    fastin.close()
else:
    print('Error: Wrong number of arguments')
