#Move all negative numbers to beginning and positive to end with constant extra space

def ref(arr):
    left=0
    right=len(arr)-1

    while(left<=right):
        if(arr[left]<0):
            left+=1

        elif(arr[right]>=0):
            right-=1

        else:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1

    return arr

#move all negative numbers to the beginning and positive numbers to the end while maintaining their original order and using constant extra space
def rearrange(arr):
    n=len(arr)
    j=0

    for i in range(n):
        if(arr[i]<0):
            arr[i],arr[j]=arr[j],arr[i]
            j+=1

    return arr


arr=[1,2,-8,3,-5,1,0,4,-2]
#ref(arr)
rearrange(arr)
print(arr)