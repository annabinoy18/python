#------TYPE1----------
#Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#Output: [1,2,2,3,5,6]

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=m-1
        j=n-1
        k=m+n-1

        while (j>=0 and i>=0):
            if(nums1[i]>nums2[j]):
                nums1[k]=nums1[i]
                k-=1
                i-=1
            else:
                nums1[k]=nums2[j]
                k-=1
                j-=1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

#------TYPE2----------
#Input: n = 4, m = 5, arr1[] = [1 3 5 7], arr2[] = [0 2 6 8 9]
#Output: arr1[] = [0 1 2 3], arr2[] = [5 6 7 8 9]

def merge(self,n,m,arr1,arr2):
    i=n-1
    j=0
    while (i>=0 and j<m):
        if(arr1[i]>arr2[j]):
            arr1[i],arr2[j]=arr2[j],arr1[i]
        i-=1
        j+=1
    arr1.sort()
    arr2.sort()
