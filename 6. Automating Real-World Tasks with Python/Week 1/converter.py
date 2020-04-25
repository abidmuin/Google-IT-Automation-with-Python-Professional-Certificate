#!/usr/bin/env python3

from PIL import Image
import os, sys

def resize_image():

    #Get the current working directory    
    dir = os.getcwd()
    input_dir = 'images'
    full_input_dir = dir + '/' + input_dir
    
    output_dir = '/opt/icons/'
    full_output_dir = dir + '/' + output_dir
    
    #Create output dir if doesn't exists
    if not os.path.exists(full_output_dir):
        os.makedirs(full_output_dir)
    
    try:
        for input_file in os.listdir(full_input_dir):
            if input_file == '.DS_Store':
                continue
            else:
                temp_file = os.path.splitext(input_file)[0]
                print("temp_file = " + str(temp_file))
                e = os.path.splitext(input_file)[1]
                print("ex = " + str(e))
                extension = '.jpeg'
                try:
                    print("Full inpur dir = " + str(full_input_dir))
                    print(input_file)
                    img = Image.open(open(full_input_dir + '/' + input_file , 'rb'))
                    img = img.rotate(-90)        
                    img = img.resize((128, 128))

                    output_file = full_output_dir + "/" + temp_file + extension
                    img.save(output_file)
                    print("Done")
                except IOError:
                    print("unable to resize image {}".format(input_file))
    except OSError:
        print('file not found')
    

if __name__ == "__main__":
    resize_image()
    
