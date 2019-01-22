# International Standard Book Number - ISBN
def rotate(nums, k):
    # bubble swap
    # [nums[i] for i range(len(nums)] = 
    # nums[:] = [nums[(i-k) % len(nums)] for i in range(len(nums))]
    k %= len(nums)
    # nums[:k], nums[k:] = nums[-k:], nums[:-k]

    def revers(nums, start, stop):
        while start<stop:
            nums[start],nums[stop] = nums[stop], nums[start]
            start += 1
            stop -= 1

    revers(nums, 0, len(nums) - 1)
    revers(nums, 0, k-1)
    revers(nums, k, len(nums)-1)

nums = [1,2,3,4,5,6]
rotate(nums, 2)
print(nums)