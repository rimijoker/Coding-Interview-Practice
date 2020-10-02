import heapq


class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        heapq.heapify(nums)
        for _ in range(len(nums)):
            out.append(heapq.heappop(nums))
        return out
