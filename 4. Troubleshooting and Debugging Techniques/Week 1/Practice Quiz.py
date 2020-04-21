import re

"""
def compare_strings(string1, string2):
    # Convert both strings to lowercase
    # and remove leading and trailing blanks
    string1 = string1.lower().strip()
    string2 = string2.lower().strip()

    # Ignore punctuation
    '''
    punctuation = r"[.?!,;:-']"
    string1 = re.sub(punctuation, r"", string1)
    string2 = re.sub(punctuation, r"", string2)
    '''

    # DEBUG CODE GOES HERE
    # print()
    # Hypen in Regex should be escaped \ should be put at first or last of the character class.
    punctuation = r"[.?!,;:\-']"
    string1 = re.sub(punctuation, r"", string1)
    string2 = re.sub(punctuation, r"", string2)

    return string1 == string2


print(compare_strings("Have a Great Day!", "Have a great day?"))  # True
print(compare_strings("It's raining again.", "its raining, again"))  # True
print(compare_strings("Learn to count: 1, 2, 3.",
                      "Learn to count: one, two, three."))  # False
print(compare_strings("They found some body.", "They found somebody."))  # False
"""

"""
def find_item(list, item):
    # Returns True if the item is in the list, False if not.
    if len(list) == 0:
        return False

    #! Sorted the given list for the Binary search operation
    list.sort()

    # Is the item in the center of the list?
    middle = len(list)//2
    if list[middle] == item:
        return True

    # Is the item in the first half of the list?
    if item < list[middle]:
        # Call the function with the first half of the list
        return find_item(list[:middle], item)
    else:
        # Call the function with the second half of the list
        return find_item(list[middle+1:], item)

    return False


# Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan",
                 "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

print(find_item(list_of_names, "Alex"))  # True
print(find_item(list_of_names, "Andrew"))  # False
print(find_item(list_of_names, "Drew"))  # True
print(find_item(list_of_names, "Jared"))  # False
"""
