#!/usr/bin/python

import os
import gzip

rootdir = '/scratch/amp/dyldo/swse.deri.org/dyldo/data'
# rootdir = '/scratch/amp/versioning/dyldo'

graphs = set()
preds = set()

print "Starting graph and pred indexing pass"
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file == 'data.nq.gz':
            print os.path.join(subdir, file)
            with gzip.open(os.path.join(subdir, file), 'rb') as f:
                g = set()
                p = set()
                for line in f:
                    graph = line.split(' ')[-2]
                    pred = line.split(' ')[2]
                    g.add(graph)
                    p.add(pred)
            # Intersect g,p with graphs,preds
            if len(graphs) == 0 and len(preds) == 0:
                graphs = g
                preds = p
            else:
                graphs = graphs.intersection(g)
                preds = preds.intersection(p)

graphs = sorted(list(graphs))
preds = sorted(list(preds))

gf = open('uniqGRAPHS', 'w')
for g in graphs:
	gf.write("%s\n" % g)
gf.close()

pf = open('uniqPREDS', 'w')
for p in preds:
	pf.write("%s\n" % p)
pf.close()

print "Starting matrix construction pass"
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        mat = {}
        if file == 'data.nq.gz':
            print os.path.join(subdir, file)
            with gzip.open(os.path.join(subdir, file), 'rb') as f:
                for line in f:
                    graph = line.split(' ')[-2]
                    pred = line.split(' ')[2]
                    if graph in graphs and pred in preds:
                        if graph not in mat:
                            mat[graph] = {pred: 1}
                        elif pred not in mat[graph]:
                            mat[graph][pred] = 1
                        else:
                            mat[graph][pred] += 1
            of = open(os.path.join(subdir, 'mat.out'), 'w')
            for g in mat:
                for pred,freq in mat[g].iteritems():
                    of.write(str(preds.index(pred)) + ":" + str(freq) + " ")
                of.write('\n')	
            of.close()

