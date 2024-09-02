#Given an array arr, rotate the array by one position in clock-wise direction.
def clck_rotate(arr):
    n=len(arr)
    last=arr[n-1]

    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=last

    return arr

#Given an array arr, rotate the array by one position in anticlock-wise direction.
def anticlck_rotate(arr):
    n=len(arr)
    frst=arr[0]

    for i in range(n-1):
        arr[i]=arr[i+1]

    arr[-1]=frst

    return arr

arr = [1, 2, 3, 4, 5]
result = anticlck_rotate(arr)
print("Array after rotating by one position:", result)

    