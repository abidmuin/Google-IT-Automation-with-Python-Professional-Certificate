#!/bin/bash

#!Assigning the matched file to "files" variable
files=$(grep " jane " ~/data/list.txt | cut -d ' ' -f 3 | cut -d '/' -f3)
echo "$files"
echo ""

#!Iterating over the files using "for loop"
destDir=~/scripts/oldFiles.txt
srcDir=~/data/list.txt
for file in $files
do
    file=~/data/$file
    echo "$file"
    #!Checking files' existence using "test" command
    if test -e $file;
        then echo "File exists";
        echo ""
        echo "$file" >> "$destDir"
    else
        echo "File doesn't exist";
        echo ""
    fi
done
