#next permutation q:15

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        
        # If there is only one element, no next permutation is possible
        if n == 1:
            return

        # Step 1: Find the last increasing position
        lastInc = -1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                lastInc = i

        # If the array is in descending order, we reverse to get the smallest lexicographical order
        if lastInc == -1:
            nums.sort()
            return

        # Step 2: Find the smallest element greater than nums[lastInc - 1] to swap with
        index = lastInc
        for i in range(lastInc, n):
            if nums[i] > nums[lastInc - 1] and nums[i] < nums[index]:
                index = i

        # Step 3: Swap elements
        nums[lastInc - 1], nums[index] = nums[index], nums[lastInc - 1]

        # Step 4: Sort the part of the array after lastInc to get the smallest possible permutation
        nums[lastInc:] = sorted(nums[lastInc:])