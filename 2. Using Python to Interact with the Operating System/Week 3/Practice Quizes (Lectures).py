"""
Fill in the code to check if the text passed contains the vowels a, e and i,
with exactly one occurrence of any other character in between.

"""


import re

"""
def check_aei(text):
    result = re.search(r"^[a|e|i]?[^aei]", text)
    return result != None


print(check_aei("academia"))  # True
print(check_aei("aerial"))  # False
print(check_aei("paramedic"))  # True
"""

"""
Fill in the code to check if the text passed contains punctuation symbols:
commas, periods, colons, semicolons, question marks, and exclamation points.

"""

'''
def check_punctuation(text):
    result = re.search(r"[,|.|:|;|?|!|]", text)
    return result != None


print(check_punctuation("This is a sentence that ends with a period."))  # True
print(check_punctuation("This is a sentence fragment without a period"))  # False
print(check_punctuation("Aren't regular expressions awesome?"))  # True
print(check_punctuation("Wow! We're really picking up some steam now!"))  # True
print(check_punctuation("End of the line"))  # False
'''

"""
Fill in the code to check if the text passed contains the vowels a, e and i,
with exactly one occurrence of any other character in between.

"""

"""
def check_aei(text):
    result = re.search(r"^[a|e|i]?[^aei]", text)
    return result != None


print(check_aei("academia"))  # True
print(check_aei("aerial"))  # False
print(check_aei("paramedic"))  # True
"""

"""
Fill in the code to check if the text passed contains punctuation symbols:
commas, periods, colons, semicolons, question marks, and exclamation points.

"""

"""
def check_punctuation(text):
    result = re.search(r"[,|.|:|;|?|!|]", text)
    return result != None


print(check_punctuation("This is a sentence that ends with a period."))  # True
print(check_punctuation("This is a sentence fragment without a period"))  # False
print(check_punctuation("Aren't regular expressions awesome?"))  # True
print(check_punctuation("Wow! We're really picking up some steam now!"))  # True
print(check_punctuation("End of the line"))  # False
"""

'''
Fill in the code to check if the text passed includes a possible U.S. zip code,
formatted as follows: exactly 5 digits, and sometimes, but not always,
followed by a dash with 4 more digits.
The zip code needs to be preceded by at least one space, and cannot be at the start of the text.
'''

'''
def check_zip_code(text):
    result = re.search(r"^[\D].*\d{5}?[-]?.*\d{4}.*", text)
    return result != None


print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False
print(check_zip_code(
    "Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code(
    "The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False
'''

'''
Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters
(including letters, numbers, and underscores) separated by one or more whitespace characters.

'''

'''
def check_character_groups(text):
    result = re.search(r"\d\s*\d", text)
    return result != None


print(check_character_groups("One"))  # False
print(check_character_groups("123  Ready Set GO"))  # True
print(check_character_groups("username user_01"))  # True
print(check_character_groups("shopping_list: milk, bread, eggs."))  # False
'''

'''
Fill in the code to check if the text passed looks like a standard sentence,
meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space,
and ends with a period, question mark, or exclamation point.
'''

'''
def check_sentence(text):
    result = re.search(r"^[A-Z][a-z0-9 ]*.[.|?|!]$", text)
    return result != None


print(check_sentence("Is this is a sentence?"))  # True
print(check_sentence("is this is a sentence?"))  # False
print(check_sentence("Hello"))  # False
print(check_sentence("1-2-3-GO!"))  # False
print(check_sentence("A star is born."))  # True
'''

'''
Fix the regular expression used in the rearrange_name function so that
it can match middle names, middle initials, as well as double surnames.
'''

'''
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*\s?\w*\.?)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])


name = rearrange_name("Kennedy, John F.")
print(name)
'''


'''
The long_words function returns all words that are at least 7 characters.
Fill in the regular expression to complete this function.
'''

'''
def long_words(text):
    pattern = r"(\w{7,})"
    result = re.findall(pattern, text)
    return result


print(long_words("I like to drink coffee in the morning."))  # ['morning']
# ['chocolate', 'afternoon']
print(long_words("I also have a taste for hot chocolate in the afternoon."))
print(long_words("I never drink tea late at night."))  # []
'''

'''
Add to the regular expression used in the extract_pid function,
to return the uppercase message in parenthesis, after the process id.
'''

'''
def extract_pid(log_line):
    regex = r"\[(\d+)\][:].*(\b[A-Z]+\b)"
    #regex = r"\[(\d+)\]: ([A-Z]+)"
    result = re.search(regex, log_line)

    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])


# 12345 (ERROR)
print(extract_pid(
    "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))
print(extract_pid("99 elephants in a [cage]"))  # None
print(extract_pid(
    "A string that also has numbers [34567] but no uppercase message"))  # None
# 67890 (RUNNING)
print(extract_pid(
    "July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"))
'''
