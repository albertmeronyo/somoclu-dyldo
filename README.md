# somoclu-dyldo

This repo contains data on some number-crunching performed on 79 snapshots of the [DyLDO dataset](http://swse.deri.org/dyldo/) to be processed by the ESOM tool [somoclu](https://github.com/peterwittek/somoclu).

The root directory contains the scripts:
- `order.py`: orders indices of sparse-matrix files
- `randbook.py`: generates a random codebook for the first somoclu map
- `somoclu.py`: runs somoclu on a set of pre-computed sparse matrices (one per DyLDO snapshot)
- `train.py`: likewise, considering the first snapshot and randomly generated codebook
- `uniqs.py`: generates lists of unique graph names and predicates, and computes the sparse matrices
- `viz.py`: generates image files for the processed maps using matplotlib/numpy (these can be pasted using e.g. `convert -delay 30 '*.png' movie.avi`)

And the data files:
- `uniqGRAPHS`: sorted unique graph names in all 79 snapshots (intersection)
- `uniqPREDS`: sorted unique predicate URIs in all 79 snapshots (intersection)

The `data` directory contains the generated sparse matrices.
