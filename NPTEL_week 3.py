#Write a function contracting(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements strictly decreases.
#>>> contracting([9,2,7,3,1])
#True

def contracting(l):
    differences = [abs(l[i] - l[i+1]) for i in range(len(l) - 1)]
    
    for i in range(len(differences) - 1):
        if differences[i] <= differences[i + 1]:
            return False
    
    return True
  

#In a list of integers l, the neighbours of l[i] are l[i-1] and l[i+1]. l[i] is a hill if it is strictly greater than its neighbours and a valley if it is strictly less than its neighbours.
#Write a function counthv(l) that takes as input a list of integers l and returns a list [hc,vc] where hc is the number of hills in l and vc is the number of valleys in l.
#>>> counthv([1,2,1,2,3,2,1])
#[2, 1]

def counthv(l):
    hc = 0  
    vc = 0 

    for i in range(1, len(l) - 1):
        if l[i] > l[i - 1] and l[i] > l[i + 1]:  # Check if it's a hill
            hc += 1
        elif l[i] < l[i - 1] and l[i] < l[i + 1]:  # Check if it's a valley
            vc += 1

    return [hc, vc]
  
#A square n×n matrix of integers can be written in Python as a list with n elements, where each element is in turn a list of n integers, representing a row of the matrix. For instance, the matrix
  #1  2  3
  #4  5  6
  #7  8  9
#would be represented as [[1,2,3], [4,5,6], [7,8,9]].
#Write a function leftrotate(m) that takes a list representation m of a square matrix as input, and returns the matrix obtained by rotating the original matrix counterclockwize by 90 degrees. For instance, if we rotate the matrix above, we get
  #3  6  9
  #2  5  8    
  #1  4  7
#Your function should not modify the argument m provided to the function rotate().
  #>>> leftrotate([[1,2,3],[4,5,6],[7,8,9]])
  #[[3, 6, 9], [2, 5, 8], [1, 4, 7]]

def leftrotate(m):
    n = len(m)
    # Create a new matrix to store the rotated result
    rotated = [[0] * n for _ in range(n)]
    
    # Fill the new matrix with the rotated values
    for i in range(n):
        for j in range(n):
            rotated[n - j - 1][i] = m[i][j]
    
    return rotated
