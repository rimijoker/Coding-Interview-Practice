class Solution(object):
    def maxSubArray(self, nums):

        current_max = nums[0]
        max_so_far = nums[0]
        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            max_so_far = max(current_max, max_so_far)
        return max_so_far
