class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = sum(nums[:3]) # result place holder        
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum_of_three = nums[i] + nums[l] + nums[r]
                # Verify conditions
                if abs(sum_of_three - target) < abs(result - target):
                    result = sum_of_three
                # Important point to check if it is equal
                # and return if it is equal and there is no better
                if sum_of_three == target:
                    return target
                elif sum_of_three <= target:
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                else:
                    r -= 1
        return result
            
        