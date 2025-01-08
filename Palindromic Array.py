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
