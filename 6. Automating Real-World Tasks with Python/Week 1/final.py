#!/usr/bin/env python3

from PIL import Image
import os, glob

dir = os.getcwd()
source_dir = dir + '/' + 'images/'
dest_dir = '/opt/icons/'

def converter():
    print("Inside converter()")
    os.chdir(source_dir)
    print("Changed Dir")
    for input_file in glob.glob("ic_*"):
        img = Image.open(source_dir + input_file)
        output_file = img.rotate(-90).resize((128,128)).convert("RGBA")
        background = Image.new('RGBA', output_file.size, (255,255,255))
        final_image = Image.alpha_composite(background, output_file).convert("RGB")
        resized_file = dest_dir + input_file
        final_image.save(resized_file, 'JPEG')

if __name__ == "__main__":
    print("main function")
    converter()

