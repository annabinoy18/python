import array

arr=array.array('i',[1,2, 3])
arr.append(6)
arr.insert(2,7)
arr.remove(2)

for i in range (len(arr)):
    print(arr[i],end=" ")
print("\r")
