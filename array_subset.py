#Given two arrays a[] and b[] of size m and n respectively, the task is to determine whether b[] is a subset of a[]. Both arrays are not sorted, and elements are distinct.

def is_subset(a, b):
    # Step 1: Create a set from array a[]
    set_a = set(a)
    
    # Step 2: Check if every element of b[] is in the set of a[]
    for element in b:
        if element not in set_a:
            return False  # If any element is not found, b[] is not a subset
    
    return True  # All elements of b[] are found in a[], so b[] is a subset

# Test case
a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]

# Output the result
print(is_subset(a, b))  # Output: True
