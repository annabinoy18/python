#Given an unsorted array arr containing both positive and negative numbers. Your task is to rearrange the array and convert it into an array of alternate positive and negative numbers without changing the relative order.

#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        pos=[]
        neg=[]
        
        for num in arr:
            if num>=0:
                pos.append(num)
            else:
                neg.append(num)
                
        posInd=0
        negInd=0
        i=0
        
        while posInd<len(pos) and negInd<len(neg):
            if i%2==0:
                arr[i]=pos[posInd]
                posInd+=1
                i+=1
            else :
                arr[i]=neg[negInd]
                negInd+=1
                i+=1
            
        while posInd < len(pos):
            arr[i]=pos[posInd]
            posInd+=1
            i+=1
            
        while negInd < len(neg):
            arr[i]=neg[negInd]
            negInd+=1
            i+=1
            
        
#second method -----------------------------------------
def right_rotate(arr,start,end):
    temp=arr(end)
    for i in range(end,start,-1):   
        arr[i]=arr[i-1]
    arr[start]=temp

def rearrange(arr):
    n=len(arr)

    for i in range(n):
        if arr[i]>=0 and i%2!=0:  # Check if the current positive element is out of place
            for j in range(i+1,n):   # Find the next negative element and rotate the subarray # between these two elements
                if arr[j]<0:
                    right_rotate(arr,i,j)
                    break
        
        elif arr[i]<0 and i%2==0:  # Check if the current negative element is out of place
            for j in range(i+1,n):  # Find the next positive element and rotate the subarray # between these two elements
                if arr[j]>=0:
                    right_rotate(arr,i,j)
                    break