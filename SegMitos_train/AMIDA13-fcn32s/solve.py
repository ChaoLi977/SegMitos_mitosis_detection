import sys
sys.path.insert(1,'/thePathToHedCaffe/')  # we use hed caffe 
import caffe
import surgery

import numpy as np
import os

#import setproctitle
#setproctitle.setproctitle(os.path.basename(os.getcwd()))

weights = '../ilsvrc-nets/vgg16-fc.caffemodel'  

# init
caffe.set_device(0)
caffe.set_mode_gpu()

solver = caffe.SGDSolver('solver.prototxt')
solver.net.copy_from(weights)

# surgeries
interp_layers = [k for k in solver.net.params.keys() if 'up' in k]
surgery.interp(solver.net, interp_layers)

solver.step(200000)
