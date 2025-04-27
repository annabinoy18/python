#mplement the KthLargest class:
#KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
#int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k,self.heap=k,nums
        heapq.heapify(self.heap)

        while len(self.heap)>self.k:
            heapq.heappop(self.heap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        if len(self.heap)>self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
