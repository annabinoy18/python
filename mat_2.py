#Given a strictly sorted 2D matrix mat[][] of size n x m and a number x. Find whether the number x is present in the matrix or not.
# Note: In a strictly sorted matrix, each row is sorted in strictly increasing order, and the first element of the ith row (i!=0) is greater than the last element of the (i-1)th row.

def searchMatrix(self, mat, x): 
    	# code here 
        row, col = len(mat), len(mat[0])

        top,bot = 0,row - 1
        while top <= bot:
            mid = (top + bot) // 2
            # Check if the target is within the current row's range
            if x < mat[mid][0]:
                bot = mid - 1
            elif x > mat[mid][col - 1]:
                top = mid + 1
            else:
                # Binary search in the row
                l, r = 0, col - 1
                while l <= r:
                    m = (l + r) // 2
                    if mat[mid][m] == x:
                        return True
                    elif mat[mid][m] < x:
                        l = m + 1
                    else:
                        r = m - 1
                return False
        
        return False
    	
