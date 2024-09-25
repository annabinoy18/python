#Given an integer array arr[]. Find the contiguous sub-array(containing at least one number) that has the maximum sum and return its sum.
def kadanes_algorithm(arr):
    # Initialize max_so_far to a very small number
    max_so_far = arr[0]  # This keeps track of the maximum sum found
    current_sum = arr[0]  # This keeps track of the sum of the current subarray
    
    # Iterate over the array starting from the second element
    for i in range(1, len(arr)):
        # Either add the current element to the current_sum or start new from arr[i]
        current_sum = max(arr[i], current_sum + arr[i])
        
        # Update max_so_far if current_sum is larger
        max_so_far = max(max_so_far, current_sum)
    
    return max_so_far
