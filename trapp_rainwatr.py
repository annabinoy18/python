def trap(arr):
    n = len(arr)
    if n <= 2:
        return 0  # No space to trap water if there are fewer than 3 blocks
    
    # Step 1: Create arrays to store the left and right max heights
    left_max = [0] * n
    right_max = [0] * n
    
    # Step 2: Fill the left_max array
    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], arr[i])
    
    # Step 3: Fill the right_max array
    right_max[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], arr[i])
    
    # Step 4: Calculate the total water trapped
    water_trapped = 0
    for i in range(n):
        water_trapped += min(left_max[i], right_max[i]) - arr[i]
    
    return water_trapped

# Example usage:
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(arr))  # Output: 6
