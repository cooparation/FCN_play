# coding = utf-8
import argparse
import Image
import os

def convert():
    file_list = os.listdir(dir)
    parser = argparse.ArgumentParser('image_dir')
    parser.add_argument()
    args
    print(file_list)
    for filename in file_list:
        path = ''
        path = dir+filename
        im = Image.open(path)
        out = im.resize((256,256),Image.ANTIALIAS)
        print "%s has been resized!"%filename
        out.save(path)

if __name__ == '__main__':
   convert()
