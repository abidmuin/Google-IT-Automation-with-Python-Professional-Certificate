'''
1. The create_python_script function creates a new python script in the current working directory,
adds the line of comments to it declared by the 'comments' variable,
and returns the size of the new file.

Fill in the gaps to create a script called "program.py".
'''

'''
from pathlib import Path


def create_python_script(filename):
    with open(filename, "w") as f:
        comments = "# Start of a new Python program"
        f.write(comments)
    with open(filename, "r") as f:
        filesize = Path(filename).stat().st_size
    return(filesize)


print(create_python_script("program.py"))
'''

'''
2. The new_directory function creates a new directory inside the current working directory,
then creates a new empty file inside the new directory,
and returns the list of files in that directory.

Complete the function to create a file "script.py" in the directory "PythonPrograms".
'''

'''
import os
def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    isDir = os.path.isdir(directory)
    if not isDir:
        os.mkdir(directory)
    # Create the new file inside of the new directory
    os.chdir(directory)
    with open(filename, "w") as f:
        pass
    # Return the list of files in the new directory
    for root, dirs, files in os.walk("."):
        for filename in files:
            return filename


print(new_directory("PythonPrograms", "script.py"))
'''
