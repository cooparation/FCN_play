# coding=utf-8
import os
import cv2
from random import shuffle
from collections import OrderedDict

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

write_lines = []
types = set()
for root, _, files in os.walk(imageSegClassDir):
    for fname in files:
        types.add(fname.split('.')[-1])
        if fname.split('.')[-1] in file_type_list:
           file_path = os.path.join(root, fname)
           write_lines.append(fname.split('.')[0] + '\n')

shuffle(write_lines)
print(types)

L  = int(len(write_lines)*0.8)
train_file = imageSetDir + '/' + 'train.txt'
f = open(train_file, 'w')
f.writelines(write_lines[:L])
f.close()

test_file = imageSetDir + '/' + 'test.txt'
f = open(test_file, 'w')
f.writelines(write_lines[L:])
f.close()

#f = open('data/food_label_name.dat','w')
#for key in filenames.keys():
#    f.write('{:25}{:5}\n'.format(key, filenames[key][0]))
#    print('{:20}{:10}{:10}'.format(key,filenames[key][0],filenames[key][1]))
#f.close()
