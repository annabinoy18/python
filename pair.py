
#Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.

class Solution:
    def getPairs(self, arr):
        # code here
        arr.sort()
        result=[]
        l,r=0,len(arr)-1

        
        while l<r:
            arr_sum=arr[l]+arr[r]
            if arr_sum==0:
                result.append([arr[l],arr[r]])
                l+=1
                r-=1
                
                while l<r and arr[l]==arr[l-1]:
                    l+=1
                while l<r and arr[r]==arr[r+1]:
                    r-=1
            
            elif arr_sum<0:
                l+=1
            else:
                r-=1
        return result    

#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        obj = Solution()
        res = obj.getPairs(arr)
        if len(res) == 0:
            print()
        else:
            IntMatrix().Print(res)
        print("~")
# } Driver Code Ends