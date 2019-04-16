import os
import sys
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

sys.path.append("../caffe/python")
import caffe
import vis

# load image, switch to BGR, subtract mean, and make dims C x H x W for Caffe

image_dir = '/apps/liusj/datasets/segDatasets/steakVOC/JPEGImages'
file_list = './data/segfoodvalid.txt'
fp = open(file_list, 'r')
for each in  fp.readlines():
    each = each.strip()
    #image_name = os.path.basename(each).split('.')[0]
    images = os.path.join(image_dir, each + '.jpg')
    print '---', images
    im = Image.open(images)
    in_ = np.array(im, dtype=np.float32)
    in_ = in_[:,:,::-1]
    in_ -= np.array((104.00698793,116.66876762,122.67891434))
    in_ = in_.transpose((2,0,1))

    # load net
    deploy = './FCN-ResNet50/fc6_size1/deploy.prototxt'
    weight = '/apps/liusj/snapshot/trainResNet_iter_90000.caffemodel'
    net = caffe.Net(deploy, weight, caffe.TEST)
    # shape for input (data blob is N x C x H x W), set data
    net.blobs['data'].reshape(1, *in_.shape)
    net.blobs['data'].data[...] = in_
    # run net and take argmax for prediction
    net.forward()
    out = net.blobs['score'].data[0].argmax(axis=0)
    print out
    out_viz = list(set(out.flat))
    print out_viz
    # visualize segmentation in PASCAL VOC colors
    num_classes = 3
    voc_palette = vis.make_palette(num_classes)
    out_im = Image.fromarray(vis.color_seg(out, voc_palette))
    image_name = (images.split('/')[-1]).split('.')[0]
    out_im.save('tmp/output_' + image_name + '.png')
    masked_im = Image.fromarray(vis.vis_seg(im, out, voc_palette))
    masked_im.save('tmp/visual_' + image_name + '.jpg')
