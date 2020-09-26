# O(log N) time | O(1) space


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            potentialMatch = nums[mid]
            leftNum = nums[left]
            rightNum = nums[right]

            if potentialMatch == target:
                return mid
            if leftNum <= potentialMatch:
                if target < potentialMatch and target >= leftNum:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > potentialMatch and target <= rightNum:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
