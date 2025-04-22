#Implement the MedianFinder class:
#MedianFinder() initializes the MedianFinder object.
#void addNum(int num) adds the integer num from the data stream to the data structure.
#double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

class MedianFinder:

    def __init__(self):
        self.small,self.large=[],[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)

        if self.small and self.large and (-self.small[0]>self.large[0]):
            val=-heapq.heappop(self.small)
            heapq.heappush(self.large,val)

        if len(self.small)>len(self.large)+1:
            val=-heapq.heappop(self.small)
            heapq.heappush(self.large,val)

        elif len(self.large)>len(self.small)+1:
            val=heapq.heappop(self.large)
            heapq.heappush(self.small,-val)

    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return -self.small[0]
        elif len(self.large)>len(self.small):
            return self.large[0]
        else:
            return (-self.small[0]+self.large[0])/2.0


