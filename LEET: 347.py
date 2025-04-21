#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map=Counter(nums)

        heap=[(-freq,num) for num,freq in freq_map.items()]
        heapq.heapify(heap)

        result=[]
        for i in range(k):
            freq,num=heapq.heappop(heap)
            result.append(num)
        return result
