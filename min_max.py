#find the minimum and maximum elements in an array

def max(arr):
    maxi=arr[0]
    for num in arr:
        if maxi<num:
            maxi=num
    return maxi

def min(arr):
    mini=arr[0]
    for num in arr:
        if mini>num:
            mini=num
    return mini

def min_max(arr):
    arr.sort()
    minmax={"min":arr[0],"max":arr[-1]}
    return minmax

# tournament method
def minmax_t(low,high,arr):
    arr_max=arr[low]
    arr_min=arr[low]

    if low==high:           #only one element
        arr_max=arr[low]
        arr_min=arr[low]
        return(arr_max,arr_min)
    
    elif high==low+1:           # only 2 elements
        if (arr[low]<arr[high]):
            arr_max=arr[high]
            arr_min=arr[low]
        else:
            arr_max=arr[low]
            arr_min=arr[high]
        return(arr_max,arr_min)

    else:
        mid=(low+high)//2
        arr_max1,arr_min1=minmax_t(low,mid,arr)
        arr_max2,arr_min2=minmax_t(mid+1,high,arr)

        return (max([arr_max1,arr_max2]), min([arr_min1,arr_min2]))
        

if __name__=="__main__":
    arr=[-2,-44,21,32,56,78,123]
    #print("max num:",max(arr))
    #print("min num:",min(arr))
    #minmax=min_max(arr)
    max_value,min_value=minmax_t(0,len(arr)-1,arr)
    print("max num:",max_value)
    print("min num:",min_value)


