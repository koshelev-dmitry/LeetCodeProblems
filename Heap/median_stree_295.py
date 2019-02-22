"""
Median is the middle value in an ordered integer list. 
If the size of the list is even, there is no middle value. 
So the median is the mean of the two middle value.
For example,
[2,3,4], the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5
Design a data structure that supports the following two operations:
void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
"""

class MedianFinder:
    import heapq
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left_max_heap = []
        self.right_min_heap = []
        
    def addNum(self, num):
        if len(self.left_max_heap) == 0:
            self.left_max_heap.append(-num)
            return
            
        if num > -self.left_max_heap[0]:
            # isert to right
            heapq.heappush(self.right_min_heap, num)
        else: 
            # insert to left
            heapq.heappush(self.left_max_heap, -num)
        
        # balance both heaps:
        if len(self.left_max_heap) > len(self.right_min_heap) + 1:
            val = heapq.heappop(self.left_max_heap)
            heapq.heappush(self.right_min_heap, -val)
        elif len(self.left_max_heap) < len(self.right_min_heap):
            val = heapq.heappop(self.right_min_heap)
            heapq.heappush(self.left_max_heap, -val)
            
    def findMedian(self):
        """
        :rtype: float
        """
        #print(self.left_max_heap)
        #print(self.right_min_heap)
        
        if len(self.left_max_heap) == len(self.right_min_heap):
            return (-self.left_max_heap[0]+self.right_min_heap[0])/2.0
        else:
            return float(-self.left_max_heap[0])
        
