#Given an array arr[] and an integer target, determine if there exists a triplet in the array whose sum equals the given target.

Return true if such a triplet exists, otherwise, return false.

def hasTripletSum(self, arr, target):
    # Step 1: Sort the array
    arr.sort()
    
    # Step 2: Iterate through each element of the array
    for i in range(len(arr) - 2):
        l, r = i + 1, len(arr) - 1  # Initialize two pointers
        
        # Step 3: Use the two-pointer technique to find a triplet
        while l < r:
            sum1 = arr[i] + arr[l] + arr[r]  # Calculate the sum of the triplet
            
            if sum1 == target:
                return True  # Triplet found
            elif sum1 < target:
                l += 1  # Increase the sum by moving the left pointer
            else:
                r -= 1  # Decrease the sum by moving the right pointer
    
    # No triplet found
    return False
