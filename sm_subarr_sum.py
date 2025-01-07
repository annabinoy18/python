#Given a number x and an array of integers arr, find the smallest subarray with sum greater than the given value. If such a subarray do not exist return 0 in that case.

def smallest_subarray_with_sum(arr, x):
    n = len(arr)
    min_length = float('inf')
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += arr[end]
        
        # Shrink the window as long as the condition is met
        while current_sum > x:
            min_length = min(min_length, end - start + 1)
            current_sum -= arr[start]
            start += 1

    return min_length if min_length != float('inf') else 0

# Example Usage
x = 51
arr = [1, 4, 45, 6, 0, 19]
print(smallest_subarray_with_sum(arr, x))  # Output: 3
