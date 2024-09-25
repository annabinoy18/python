#Given an array arr[] denoting heights of N towers and a positive integer K.

#For each tower, you must perform exactly one of the following operations exactly once.

#Increase the height of the tower by K
#Decrease the height of the tower by K
#Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.
#Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.

def getMinDiff(n, arr,k):
            arr.sort()
            ans = arr[n - 1] - arr[0]  # Maximum possible height difference
         
            tempmin = arr[0]
            tempmax = arr[n - 1]
         
            for i in range(1, n):
                if arr[i] < k:
                    continue
                tempmin = min(arr[0] + k, arr[i] - k)
         
                # Minimum element when we
                # add k to whole array
                # Maximum element when we
                tempmax = max(arr[i - 1] + k, arr[n - 1] - k)
         
                # subtract k from whole array
                ans = min(ans, tempmax - tempmin)
         
            return ans
         
