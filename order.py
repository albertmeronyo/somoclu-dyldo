#!/usr/bin/python

import os

rootdir = '/scratch/amp/dyldo/swse.deri.org/dyldo/data'
# rootdir = '/scratch/amp/versioning/dyldo'

print "Ordering matrices"
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file == 'mat.out':
            print os.path.join(subdir, file)
            with open(os.path.join(subdir, file), 'rb') as f:
                with open(os.path.join(subdir, 'mat.sorted.out'), 'w') as of:
                    for line in f:
                        of.write(" ".join(sorted(line.split(),key=lambda x: int(x.split(':')[0]))))
                        of.write('\n')
              
