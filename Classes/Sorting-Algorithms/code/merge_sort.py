def merge_sort(list):
    '''
    sort list in ascending
    return sorted list
    '''
    if len(list) <= 1:
        return list
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)


def split(list):
    '''
    divide unsorted lists at midpoint into sublists
    return left, right
    '''
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    
    return left,right

def merge(left, right):
    '''
    merges 2 lists while sorting them
    returns merged list
    '''
    l = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1
    
    while i < len(left):
        l.append(left[i])
        i+=1
    while j < len(right):
        l.append(right[j])
        j+=1
    
    return l

def verify_sorted(list):
    n = len(list)
    
    if n == 0 or n == 1:
        return True
    return list[0] < list[1] and verify_sorted(list[1:])

arr = [23, 2, 34, 56, 100, 67, 5, 75, 45]

l = merge_sort(arr)

print(verify_sorted(l))
print(l)