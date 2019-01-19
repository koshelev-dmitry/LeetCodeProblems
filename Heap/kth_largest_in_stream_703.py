class KthLargest(object):
    import heapq
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap_min = nums
        self.k = k
        heapq.heapify(self.heap_min)
        while len(self.heap_min) > k:
            heapq.heappop(self.heap_min)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap_min) < self.k:
            heapq.heappush(self.heap_min, val)
        elif val > self.heap_min[0]:
            heapq.heappushpop(self.heap_min, val)
        return self.heap_min[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)