def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns - 1."""
    # ? i represents index of the list
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1
