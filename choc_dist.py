#Given an array arr[] of positive integers, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets among m students such that -
    #  i. Each student gets exactly one packet.
   #  ii. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum and return that minimum possible difference.

def distribute_chocolates(arr, m):
    # Step 1: Sort the array of chocolates
    arr.sort()
    
    # If there are fewer packets than students, return -1 as it's not possible to distribute
    if len(arr) < m:
        return -1
    
    # Step 2: Initialize the minimum difference as a large number
    min_diff = float('inf')
    
    # Step 3: Slide a window of size m over the sorted array using the new loop condition
    n = len(arr)
    for i in range(n - m + 1):  # This ensures i + m - 1 < n
        # Calculate the difference between the max and min chocolates in this window
        current_diff = arr[i + m - 1] - arr[i]
        
        # Update the minimum difference
        min_diff = min(min_diff, current_diff)
    
    return min_diff

# Example usage:
arr = [12, 4, 7, 9, 2, 23, 25, 41, 40, 40, 28, 42, 30, 40, 40]
m = 7
print(distribute_chocolates(arr, m))  # Output: 10
