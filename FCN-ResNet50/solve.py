import sys
sys.path.append('../caffe/python')
import caffe
import surgery, score

import numpy as np
import os

try:
    import setproctitle
    setproctitle.setproctitle(os.path.basename(os.getcwd()))
except:
    pass

weights = './models/fc6_size1.caffemodel'
#weights = './snapshot/train_iter_2000.solverstate'

# init
caffe.set_device(int(sys.argv[1]))
caffe.set_mode_gpu()

solver = caffe.SGDSolver('./FCN-ResNet50/fc6_size1/solver.prototxt')
solver.net.copy_from(weights)

# scoring
#val = np.loadtxt('./data/seg11valid.txt', dtype=str)
val = np.loadtxt('./data/segfoodvalid.txt', dtype=str)

for _ in range(25):
    solver.step(4000)
    score.seg_tests(solver, False, val, layer='score')
