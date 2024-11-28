def quick_sort(arr):
    if len(arr) <=1:
        return arr
    midpoint = arr[len(arr) // 2]
    
    left = [x for x in arr if x < midpoint]
    middle = [x for x in arr if x == midpoint]
    right = [x for x in arr if x > midpoint]
    
    return quick_sort(left) + middle + quick_sort(right)


arr = [4, 7, 2, 9, 8, 10]
print (quick_sort(arr))