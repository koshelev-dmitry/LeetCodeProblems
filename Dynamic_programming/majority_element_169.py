class Solution:
    def majorityElement(self, nums):
        # if len(nums) == 1:
        #     return nums[0]
        # hash_table = {}
        # for num in nums:
        #     if num in hash_table:
        #         hash_table[num] += 1
        #         if hash_table[num] > len(nums) // 2:
        #             return num
        #     else:
        #         hash_table[num] = 1
        # return None
        import collections
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

        # Boyer-Moore Voting Algorithm
        # very clever idea
        # count = 0
        # candidate = None

        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #     count += (1 if num == candidate else -1)

        # return candidate

print(Solution().majorityElement([1,1,1,1,1,2,2,3,5,4,4,4,4,]))