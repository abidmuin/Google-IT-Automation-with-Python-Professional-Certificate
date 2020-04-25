#!/usr/bin/env python3

import glob
import os
from PIL import Image
import os.path
from os import path


def main():
    print("Is it File?" + str(path.isfile(
        '/home/n1ghtmar3/Desktop/Qwiklabs/Week_1/images/ic_add_location_black_48dp')))
    print("Is it File?" + str(path.isdir('/home/n1ghtmar3/Desktop/Qwiklabs/Week_1/images/ic_add_location_black_48dp')))


if __name__ == "__main__":
    main()

"""
path = "/root/Desktop/python/images/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((200,200), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()
"""

# Another one

#!/usr/bin/env python3


def convert():
    print("Inside")

    for item in glob.glob("ic_*"):
        print(item)
        img = Image.open(item).convert('RGB')
        print("Check")
        img.rotate(-90).resize((128, 128)).save("/opt/icons/" + item, "JPEG"),
        print("Success!")


if __name__ == "__main__":
    convert()


#################################################
    """
        if infile[0] == ".":
            continue
        im = Image.open(source_dir + infile)
        out = im.rotate(90).resize((128,128)).convert("RGBA")
        background = Image.new('RGBA', out.size, (255,255,255))
        final = Image.alpha_composite(background, out).convert("RGB")
        new_file = new_dir + infile
        final.save(new_file, 'JPEG', quality=80)
    """
