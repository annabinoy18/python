Given an array of integers, arr[]. Find if there is a subarray (of size at least one) with 0 sum. Return true/false depending upon whether there is a subarray present with 0-sum or not

def has_zero_sum_subarray(arr):
    prefix_sum, seen_sums = 0, set()  # Initialize prefix_sum to 0 and an empty set to track sums
    for num in arr:                   # Iterate through each element in the array
        prefix_sum += num             # Add the current element to the prefix sum
        if prefix_sum == 0 or prefix_sum in seen_sums:  # Check conditions for a zero-sum subarray
            return True               # If either condition is met, a zero-sum subarray exists
        seen_sums.add(prefix_sum)     # Otherwise, add the current prefix sum to the set
    return False                      # If loop completes without returning, no zero-sum subarray exists


def has_given_sum_subarray(arr, target_sum):
    prefix_sum = 0
    seen_sums = set()
    
    for num in arr:
        prefix_sum += num
        # Check if there is a subarray with the given sum
        if prefix_sum == target_sum or (prefix_sum - target_sum) in seen_sums:
            return True
        seen_sums.add(prefix_sum)
    
    return False
