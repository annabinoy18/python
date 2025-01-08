#Given an array arr and a number k. One can apply a swap operation on the array any number of times, i.e choose any two index i and j (i < j) and swap arr[i] , arr[j] . Find the minimum number of swaps required to bring all the numbers less than or equal to k together, i.e. make them a contiguous subarray.

def min_swaps(arr, k):
    # Step 1: Count elements <= k
    count_k = sum(1 for x in arr if x <= k)
    
    # If there are no elements <= k, no swaps are needed
    if count_k == 0:
        return 0
    
    # Step 2: Count bad elements in the first window of size count_k
    bad = sum(1 for i in range(count_k) if arr[i] > k)
    
    # Initialize the result with the count of bad elements in the first window
    min_swaps = bad
    
    # Step 3: Slide the window
    n = len(arr)
    for i in range(count_k, n):
        # Include the next element in the window
        if arr[i] > k:
            bad += 1
        # Exclude the previous element from the window
        if arr[i - count_k] > k:
            bad -= 1
        
        # Update the minimum swaps required
        min_swaps = min(min_swaps, bad)
    
    return min_swaps

# Example usage
arr = [2, 1, 5, 6, 3]
k = 3
print("Minimum swaps required:", min_swaps(arr, k))
