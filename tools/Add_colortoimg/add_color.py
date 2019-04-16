#!usr/bin/python
# -*- coding:utf-8 -*-
import argparse
import os
import PIL.Image
import numpy as np
from skimage import io,data,color


def main():
    label_save_dir = '/home/hp/data/steak/iron_plate/bottom_segmentation'
    if not os.path.exists(label_save_dir):
        os.mkdir(label_save_dir)

    parser = argparse.ArgumentParser()
    parser.add_argument('json_file_list')
    args = parser.parse_args()
    json_file_list = args.json_file_list
    fp = open(json_file_list, 'r')

    for eachline in fp.readlines():
        json_file = eachline.strip()
        label_dir = os.path.basename(json_file).replace('.', '_')
        label_dir = os.path.join(os.path.dirname(json_file), label_dir)
        if not os.path.exists(label_dir):
            print 'label_dir', label_dir, 'not exists'
            continue
        img_file = os.path.join(label_dir, 'label.png')
        img = PIL.Image.open(img_file)
        img = np.array(img)
        dst = color.label2rgb(img, bg_label=0, bg_color=(0, 0, 0))

        label_image_name = (os.path.basename(json_file).split('.'))[0]
        label_image_name += '.png'
        img_save = os.path.join(label_save_dir, label_image_name)
        io.imsave(img_save, dst)
        print 'label image save to', img_save

    fp.close()

if __name__ == '__main__':
    main()
