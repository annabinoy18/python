#You are given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
#If there are no such elements return an empty array. In this case, the output will be -1.

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        #Code Here
        i,j,k=0,0,0
        n1=len(arr1)
        n2=len(arr2)
        n3=len(arr3)
        result=[]
        last_added=0
        
        while i<n1 and j<n2 and k<n3:
            if (arr1[i]==arr2[j] and arr2[j]==arr3[k]):
                if last_added != arr1[i]:
                    result.append(arr1[i])
                    last_added = arr1[i]
                i+=1
                j+=1
                k+=1
                
            elif arr1[i]<arr2[j]:
                i+=1
            elif arr2[j]<arr3[k]:
                j+=1
            else:
                k+=1
        if len(result) == 0:
            return [-1]
        else :
            return result
     
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        brr = list(map(int, input().split()))
        crr = list(map(int, input().split()))
        ob = Solution()
        res = ob.commonElements(arr, brr, crr)
        if len(res) == 0:
            print(-1)
        else:
            print(" ".join(map(str, res)))

# } Driver Code Ends