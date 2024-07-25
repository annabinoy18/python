def printSubArrays(arr, start, end):
    
    if end == len(arr):
        return
    
    elif start > end:
        return printSubArrays(arr, 0, end + 1)

    else:
        print(arr[start:end + 1])
        return printSubArrays(arr, start + 1, end)

def main():
    user_input=input('enter the elements in the array')

    arr=[int(x) for x in user_input.split()]

    printSubArrays(arr,0,0)

if __name__=='__main__':
    main()


