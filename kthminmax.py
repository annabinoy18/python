# find the kth largest/smallest element in the array without using inbuilt sorting

def klargest(arr,k):
    k = len(arr)-1   #largest
    #k=k-1        smallest

    def quickSelect(l,r):
        pivot=arr[r]
        p=l

        for i in range(l,r):
            if arr[i] <= pivot:
                arr[p],arr[i]=arr[i],arr[p]
                p += 1
        arr[p],arr[r]=arr[r],arr[p]

        if p > k:
            return quickSelect(l,p-1)
        elif p<k:
            return quickSelect(p+1,r)
        else:
            return arr[p]
            
    return quickSelect(0, len(arr)-1 )

if __name__== "__main__":
    arr=[2,5,3,7,5,8,9]
    k=2
    maxnum=klargest(arr,k)
    print("max num:",maxnum)