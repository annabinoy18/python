#Given an array arr[] of non-negative integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.

def longestConsecutive(arr):
    # Step 1: Convert array to a set for uniqueness and faster lookup
    num_set = set(arr)
    
    # Step 2: Initialize the variable to store the maximum length of subsequence
    longest = 0
    
    # Step 3: Iterate through the set to find the longest consecutive subsequence
    for num in num_set:
        # Only check for the start of a sequence (when num-1 is not in the set)
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            # Find the length of the current consecutive sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            # Update the longest sequence length
            longest = max(longest, current_streak)
    
    return longest

# Example Usage
arr = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(arr))  # Output: 4 (subsequence [1, 2, 3, 4])

arr = [0, 1, 2, 3, 4, 5]
print(longestConsecutive(arr))  # Output: 6 (subsequence [0, 1, 2, 3, 4, 5])
