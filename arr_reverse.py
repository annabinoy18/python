def rev_Extra_Arr(arr):
    rev_arr=arr[::-1]

    print('reversed array 0: ') #non in place
    #for i in rev_arr:
    #    print(i,end=" ")
    print(rev_arr)
    print ()

def rev_loop (arr,start,end): #in place
    while start < end:
        arr[start],arr[end]=arr[end],arr[start]
        start += 1
        end -=1

    print('reversed array 1: ')
    for i in arr:
        print(i,end=" ")
    print ()

def rev_inbuild(arr): #in place
    rev_arr=list(reversed(arr))

    print('reversed arr 2 ' )
    print(rev_arr)
    print ('\r')

def rev_recursion(arr,start,end): #in-place or non in place
    if start>=end:
       return
    arr[start],arr[end]=arr[end],arr[start]
    rev_recursion(arr,start+1,end-1)

    print('reversed arr 3 ' )
    print(arr)
    print ()



user_inp=input('enter the elements of the array')
arr=[int(x) for x in user_inp.split()]
start=0
end=len(arr)-1
rev_Extra_Arr(arr)
rev_loop(arr,start,end)
rev_inbuild(arr)
rev_recursion(arr,start,end)

