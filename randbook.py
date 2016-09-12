#!/usr/bin/python

import random

outfile = 'initial-codebook.wts'
neurons = 375
dimensions = 275412

random.seed()

with open(outfile, 'w') as f:
    f.write('%15 25\n')
    f.write('%275412\n')
    for i in range(neurons):
        for j in range(dimensions):
            f.write("%.10f" % random.uniform(-1, 1) + " ")
        f.write('\n')
