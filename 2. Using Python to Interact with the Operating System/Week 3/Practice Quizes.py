'''
1. The check_web_address function checks if the text passed qualifies as a top-level web address, 
meaning that it contains alphanumeric characters (which includes letters, numbers, and 
underscores), as well as periods, dashes, and a plus sign, followed by a period 
and a character-only top-level domain such as ".com", ".info", ".edu", etc. 

Fill in the regular expression to do that, using escape characters, wildcards, repetition qualifiers, 
beginning and end-of-line characters, and character classes.

'''

import re

'''
def check_web_address(text):
    pattern = r"^\w*[-]*.*\.(com|org|edu|info|US)$"
    result = re.search(pattern, text)
    return result != None


print(check_web_address("gmail.com"))  # True
print(check_web_address("www@google"))  # False
print(check_web_address("www.Coursera.org"))  # True
print(check_web_address("web-address.com/homepage"))  # False
print(check_web_address("My_Favorite-Blog.US"))  # True
'''

'''
2. The check_time function checks for the time format of a 12-hour clock, as follows: 
the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, 
then an optional space, and then AM or PM, in upper or lower case. Fill in the regular expression to do that. 

How many of the concepts that you just learned can you use here?

'''

'''
def check_time(text):
    pattern = r"^[1-9][0-2]?[:][0-5][0-9]?[ ]?(pm|am)$"
    result = re.search(pattern, text, re.IGNORECASE)
    return result != None


print(check_time("12:45pm"))  # True
print(check_time("9:59 AM"))  # True
print(check_time("6:60am"))  # False
print(check_time("five o'clock"))  # False
'''

'''
3. The contains_acronym function checks the text for the presence of 2 or more characters or 
digits surrounded by parentheses, with at least the first character in uppercase (if it's a letter), 
returning True if the condition is met, or False otherwise. 
For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication" 
should return True since (IM) satisfies the match conditions." 

Fill in the regular expression in this function:

'''

'''
def contains_acronym(text):
    pattern = r"[(][\w]{2,}]*[)]"
    result = re.search(pattern, text)
    return result != None


print(contains_acronym(
    "Instant messaging (IM) is a set of communication technologies used for text-based communication"))  # True
print(contains_acronym(
    "American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication"))  # True
print(contains_acronym("Please do NOT enter without permission!"))  # False
print(contains_acronym(
    "PostScript is a fourth-generation programming language (4GL)"))  # True
print(contains_acronym(
    "Have fun using a self-contained underwater breathing apparatus (Scuba)!"))  # True
'''

'''
3. We're working with a CSV file, which contains employee information. 
Each record has a name field, followed by a phone number field, and a role field. 
The phone number field contains U.S. phone numbers, and needs to be modified to the 
international format, with "+1-" in front of the phone number. 
Fill in the regular expression, using groups, to use the transform_record function to do that.
'''


def transform_record(record):
    new_record = re.sub(___)
    return new_record


print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist"))
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# Charlie Rivera,+1-698-746-3357,Web Developer
