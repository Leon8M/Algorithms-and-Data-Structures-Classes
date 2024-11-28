def linear_search(list, target):
    """
    Returns the index of target if found in list, else None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    """
    Returns Not found if the index is None, else index
    """
    if index is not None:
        print ("Found at index: ", index)
    else:
        print ("Target not found: ")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)