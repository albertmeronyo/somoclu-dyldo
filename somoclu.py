#!/usr/bin/python
# Runs somoclu initializing with the codelist of the previous epoch

import os
from subprocess import call

first = '2012-05-13'
path = '/home/amp/ssd/mats'
suffix = '-mat.out.sorted'
previous = '2012-05-13'
out_suffix = suffix + '.rgb.wts'
this_suffix = '.rgb'

for dirname, firnmaes, filenames in os.walk(path):
    for filename in sorted(filenames):
        if filename.endswith(suffix):
            if first not in filename:
                call('somoclu -k 2 -x 25 -y 15 -c ' + previous + out_suffix + ' -l 0.05 -e 3 -t exponential -r 5 ' + filename + ' ' + filename + this_suffix, shell=True)
                # print 'somoclu -k 2 -x 25 -y 15 -c ' + previous + out_suffix + ' -l 0.05 ' + filename + ' ' + filename + this_suffix
            previous = filename[0:10]
