#Given an array arr[] of positive integers. Return true if all the array elements are palindrome otherwise, return false.

def isPalinArray(arr):
    # Code here
    def isPalindrome(num):
        if str(num)==str(num)[::-1] :
            return True
        else:
            return False
    
    for num in arr:
        if isPalindrome(num)==False:
            return False
        
    return True

#Minimum no. of operations required to make an array palindrome code
def min_operations_to_make_palindrome(arr):
    n = len(arr)
    operations = 0
    
    # Traverse only till the middle of the array
    for i in range(n // 2):
        # Compare arr[i] with arr[n-i-1]
        if arr[i] != arr[n - i - 1]:
            # If they are not equal, we need one operation to match them
            operations += 1
            
    return operations

# Example usage
arr1 = [1, 2, 3, 2, 1]
print(min_operations_to_make_palindrome(arr1))  # Output: 0 (Already a palindrome)

arr2 = [1, 2, 3, 4, 5]
print(min_operations_to_make_palindrome(arr2))  # Output: 2 (Change 2 to 4 and 3 to 3)

arr3 = [1, 3, 2, 2, 1]
print(min_operations_to_make_palindrome(arr3))  # Output: 1 (Change 3 to 2)
