#!/usr/bin/python

import argparse
import json
import os
import os.path as osp

import PIL.Image
import yaml

from labelme import utils


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('json_file_list')
    args = parser.parse_args()

    json_file_list = args.json_file_list
    fp = open(json_file_list, 'r')
    #json_file = args.json_file
    for eachline in fp.readlines():
        json_file = eachline.strip()

        out_dir = osp.basename(json_file).replace('.', '_')
        out_dir = osp.join(osp.dirname(json_file), out_dir)
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)

        data = json.load(open(json_file))

        img = utils.img_b64_to_array(data['imageData'])
        lbl, lbl_names = utils.labelme_shapes_to_label(img.shape, data['shapes'])

        lbl_viz = utils.draw_label(lbl, img, lbl_names)

        PIL.Image.fromarray(img).save(osp.join(out_dir, 'img.png'))
        PIL.Image.fromarray(lbl).save(osp.join(out_dir, 'label.png'))
        PIL.Image.fromarray(lbl_viz).save(osp.join(out_dir, 'label_viz.png'))

        info = dict(label_names=lbl_names)

        with open(osp.join(out_dir, 'info.yaml'), 'w') as f:
            yaml.safe_dump(info, f, default_flow_style=False)

        print('wrote data to %s' % out_dir)
    fp.close()


if __name__ == '__main__':
    main()
