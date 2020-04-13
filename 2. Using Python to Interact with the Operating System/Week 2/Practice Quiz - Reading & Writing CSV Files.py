"""
We're working with a list of flowers and some information about each one.
The create_file function writes this information to a CSV file.
The contents_of_file function reads this file into records and returns the information in a nicely formatted block.

Fill in the gaps of the contents_of_file function to turn the data in the CSV file into a dictionary using DictReader.
"""

import os
import csv

"""
# Create a file with data in it


def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row


def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename) as flowers:
        # Read the rows of the file into a dictionary
        reader = csv.DictReader(flowers)
        # Process each item of the dictionary
        for row in reader:
            return_string += "a {} {} is {}\n".format(
                row["color"], row["name"], row["type"])

    return return_string


# Call the function
print(contents_of_file("flowers.csv"))
"""

"""
Using the CSV file of flowers again, 

fill in the gaps of the contents_of_file function to process the data without turning it into a dictionary. 
How do you skip over the header record with the field names?
"""

"""
# Create a file with data in it

def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row


def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename, "r+") as flowers:
        # Read the rows of the file
        rows = csv.reader(flowers)
        next(rows)  # Skips the CSV header
        # Process each row
        for row in rows:
            name, color, type = row
            # Format the return string for data rows only
            return_string += "a {} {} is {}\n".format(color, name, type)
    return return_string


# Call the function
print(contents_of_file("flowers.csv"))

"""
