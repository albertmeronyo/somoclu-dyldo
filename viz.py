#!/usr/bin/python

import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

import somoclu
import os
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

n_rows, n_columns = 15, 25
path = '/home/amp/ssd/mats'
suffix = '.wts'
exp_count = 3

for dirname, firnmaes, filenames in os.walk(path):
    for filename in sorted(filenames):
        if filename.endswith(suffix):
            print 'Initializing epoch...'
            som = somoclu.Somoclu(n_columns, n_rows, maptype="toroid")
            print 'Loading codebook at ' + os.path.join(dirname,filename)

            som.load_codebook(os.path.join(dirname,filename))
            som.load_bmus(os.path.join(dirname, filename.replace('.wts', '.bm')))
            som.load_umatrix(os.path.join(dirname, filename.replace('.wts', '.umx')))
            # print 'SOM loaded with ' + str(len(som)) + ' instances'

            print 'Saving viz...'
            colors = ["red"] * 50
            with open(os.path.join(dirname, filename.replace('.wts', '.bm'))) as f:
                instances = int(f.readlines()[1].split('%')[1].split('\n')[0])
            print 'BMUs have ' + str(instances) + ' labels'
            som.view_umatrix(bestmatches=True, labels=range(instances), filename=os.path.join(dirname, filename.replace('.wts', '.' + str(exp_count) + '.png')))
