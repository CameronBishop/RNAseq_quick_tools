import sys
if len(sys.argv) == 2:
    output = open('.'.join(sys.argv[1].split('.')[:-1]) + '_long_form.txt', 'w+')

    with open(sys.argv[1], encoding = 'ISO-8859-1') as gmt_in:  # the encoding of the GMT is ISO-8859-1, whcih is not default so must specify

        inlist = gmt_in.readlines()

    sets = []
    genes = []
    for i, value in enumerate(inlist):      # parse gmt
        value = value.strip('\n')             
        line = value.split('\t')            # split each line into a list, and take all elements except first two  
        
        num = len(line[2:])                 # record what set each gene belongs to 
        sets.extend([line[0]] * num)
        genes.extend(line[2:]) 

    output.write('GENE' + '\t' + 'SET' + '\n')
    for k, val in enumerate(genes):                             # write columns to a file
        output.write(genes[k] + '\t' + sets[k] + '\n')

else:
    print('\n', 'Error: Wrong number of arguments', '\n')
