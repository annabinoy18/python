#Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

def maxProduct(arr):
    # Initialize variables
    max_product = arr[0]
    min_product = arr[0]
    result = arr[0]
    
    # Traverse the array starting from the second element
    for i in range(1, len(arr)):
        num = arr[i]
        
        # If the current number is negative, swap max_product and min_product
        if num < 0:
            max_product, min_product = min_product, max_product
        
        # Update max_product and min_product
        max_product = max(num, num * max_product)
        min_product = min(num, num * min_product)
        
        # Update the result to track the maximum product so far
        result = max(result, max_product)
    
    return result

# Example Usage
arr = [2, 3, -2, 4]
print(maxProduct(arr))  # Output: 6 (subarray [2, 3] has the maximum product)

arr = [-2, 0, -1]
print(maxProduct(arr))  # Output: 0 (subarray [0] has the maximum product)
