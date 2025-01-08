#Given an array arr[] of integers, calculate the median.

def calculate_median(arr):
    # Step 1: Sort the array
    arr.sort()
    
    # Step 2: Find the median based on the number of elements
    n = len(arr)
    if n % 2 == 1:
        # Odd number of elements: return the middle element
        return arr[n // 2]
    else:
        # Even number of elements: return the average of the two middle elements
        return (arr[n // 2 - 1] + arr[n // 2]) / 2

# Example usage
arr = [7, 1, 3, 4, 5]
print("Median:", calculate_median(arr))

arr = [7, 1, 3, 4]
print("Median:", calculate_median(arr))


