#!/usr/bin/env python3

from PIL import Image
import os
import glob

dir = os.getcwd()
source_dir = dir + '/Desktop/test_data/'
dest_dir = dir + '/Desktop/resized_test_data/'
size = 128, 128


def image_resize():
    os.chdir(source_dir)
    for input_file in glob.glob("*"):
        try:
            img = Image.open(input_file)
            print("{} image file is opened!".format(input_file))
        except:
            print("Could not read the image file! {}".format(input_file))

        resized_image = img.resize((size))
        os.chdir(dest_dir)

        try:
            resized_image.save(input_file)
            print("{} is resized to {}".format(input_file, size))
        except:
            print("Error saving {}".format(input_file))


if __name__ == "__main__":
    image_resize()
