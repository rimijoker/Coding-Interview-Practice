# O(log N) time | O(1) space


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = self.findStart(nums, target, 0, len(nums) - 1)
        end = self.findEnd(nums, target, 0, len(nums) - 1)
        return [start, end]

    def findStart(self, nums, target, left, right):
        start = -1
        while left <= right:
            mid = (left + right) // 2
            midNum = nums[mid]
            if midNum == target:
                start = mid
                right = mid - 1
            elif target < midNum:
                right = mid - 1
            elif target > midNum:
                left = mid + 1
        return start

    def findEnd(self, nums, target, left, right):
        end = -1
        while left <= right:
            mid = (left + right) // 2
            midNum = nums[mid]
            if midNum == target:
                end = mid
                left = mid + 1
            elif target < midNum:
                right = mid - 1
            elif target > midNum:
                left = mid + 1
        return end
