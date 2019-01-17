class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if nums1 == []:
            if len(nums2)%2 == 1: # 7; 7//2 = 3; 8//2=4,3
                return nums2[len(nums2)//2]
            else:
                return (nums2[len(nums2)//2 - 1] + nums2[len(nums2)//2])/2
        if nums2 == []:
            if len(nums1)%2 == 1: # 7; 7//2 = 3; 8//2=4,3
                return nums1[len(nums1)//2]
            else:
                return (nums1[len(nums1)//2 - 1] + nums1[len(nums1)//2])/2

        median_position = (len(nums1) + len(nums2) - 1)//2
        cur1 = 0
        cur2 = 0
        last_value_in_merged = None
        while cur1 + cur2 <= median_position:
            if cur1 < len(nums1) and cur2 < len(nums2):
                if nums1[cur1] <= nums2[cur2]:
                    last_value_in_merged = nums1[cur1]
                    cur1 += 1
                else:
                    last_value_in_merged = nums2[cur2]
                    cur2 += 1
            else: 
                if cur1 < len(nums1):
                    last_value_in_merged = nums1[cur1]
                    cur1 += 1
                elif cur2 < len(nums2):
                    last_value_in_merged = nums2[cur2]
                    cur2 += 1
            
        # we are near the median position:
        if len(nums1)+len(nums2) == 2:
            return (nums1[0]+nums2[0])/2
        elif (len(nums1) + len(nums2)) % 2 == 1:
            return last_value_in_merged
        else:
            previous_value = last_value_in_merged
            if cur1 < len(nums1) and cur2 < len(nums2):
                if nums1[cur1] <= nums2[cur2]:
                    last_value_in_merged = nums1[cur1]
                else:
                    last_value_in_merged = nums2[cur2]
            else: 
                if cur1 < len(nums1):
                    last_value_in_merged = nums1[cur1]
                elif cur2 < len(nums2):
                    last_value_in_merged = nums2[cur2]
            return (last_value_in_merged + previous_value)/2


solution = Solution()
nums1 = [2,3]
nums2 = [1]

print(solution.findMedianSortedArrays(nums1, nums2))
