#!/usr/bin/python
import argparse
import base64
try:
    import io
except ImportError:
    import io as io
import json
import os
import os.path as osp

import numpy as np
import PIL.Image
import yaml

from labelme import utils

def b64_jsonImageData2Array(img_b64):
    f = io.BytesIO()
    f.write(base64.b64decode(img_b64))
    img_arr = np.array(PIL.Image.open(f))
    return img_arr

def getShapeLabels(img_shape, shapes, label_name_to_val):
    for shape in sorted(shapes, key=lambda x:x['label']):
        label_name = shape['label']
        if label_name in label_name_to_val:
            label_value = label_name_to_val[label_name]
        else:
            label_value = len(label_name_to_val)
            label_name_to_val[label_name] = label_value
    #return label_name_to_val

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('json_file_dir')
    args = parser.parse_args()

    json_file_dir = args.json_file_dir
    json_file_list = 'json_file_list.txt'
    fp = open(json_file_list, 'w')
    label_name_value = {'background':0}
    for dir_info in os.walk(json_file_dir):
        root_dir, sub_dir, json_files = dir_info
        for each_file  in json_files:
            if cmp(each_file.split('.')[-1], 'json') != 0:
                print 'ignore', each_file
                continue
            num_images += 1
            json_file = os.path.join(root_dir, each_file)
            json_file = os.path.abspath(json_file)
            fp.write(json_file + '\n')

            data = json.load(open(json_file))

            img = b64_jsonImageData2Array(data['imageData'])
            getShapeLabels(img.shape, data['shapes'], label_name_value)

    # print label info
    fp.close()
    fp = open('name_value.txt', 'w')
    for label_name, label_value in label_name_value.items():
        print('{:20}{:8}'.format(label_name, label_value))
        fp.write('{:20}{:8}\n'.format(label_name, label_value))
    fp.close()

if __name__ == '__main__':
    main()
