def union_count(arr1, arr2):
    # Convert both arrays to sets
    set1 = set(arr1)
    set2 = set(arr2)
    
    # Perform the union operation
    union_set = set1.union(set2)
    
    # Return the number of elements in the union
    return len(union_set)

def intersection_count(arr1,arr2):
    set1 = set(arr1)
    set2 = set(arr2)

    intersection_set=set1.intersection(set2)

    return len(intersection_set)