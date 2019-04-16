# coding=utf-8
import os
import cv2
from random import shuffle
from collections import OrderedDict
import shutil

image_root_dir = '/apps/liusj/datasets/segDatasets/steakVOC'
imageJpegsDir = image_root_dir + '/' + 'JPEGImages'
imageSetDir = image_root_dir + '/' + 'ImageSets' + '/' + 'Segmentation'
imageSegClassDir = image_root_dir + '/' + 'SegmentationClass'
file_type_list =['GIF', 'gif', 'jpeg',  'bmp', 'png', 'JPG',  'jpg', 'JPEG']

if not os.path.exists(imageSetDir):
    os.makedirs(imageSetDir)

filenames = OrderedDict()
## write the class name lists with manual
# [label_name label_index image_num]

labelPng = '/apps/liusj/datasets/segDatasets/steak/iron_plate/bottom_label'
for root, _, files in os.walk(labelPng):
    for fname in files:
        fname = os.path.basename(fname)
        if fname == 'label.png':
           file_path = os.path.join(root, fname)
           imageName = file_path.split('/')[-2].replace('_json', '')
           dst_path = os.path.join(imageSegClassDir, imageName + '.png')
           print 'src', file_path
           print 'dst', dst_path
           shutil.copy(file_path, dst_path)

