class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        return sorted(nums)[-k]
        """
        import heapq
        heap_k_size = list(nums[:k])
        heapq.heapify(heap_k_size)
        for i in range(k, len(nums)):
            if nums[i] > heap_k_size[0]:
                heapq.heapreplace(heap_k_size, nums[i])
        return heap_k_size[0]
        # return heapq.nlargest(k, nums)[-1] 
        # from docs: nlargest is equivalent of 
        # sorted(iterable)[:k], which is not the same
        