# O(N) time | O(1) space


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        area = float("-inf")
        start, end = 0, size - 1
        while start < end:
            area = max(area, ((end - start) * min(height[start], height[end])))
            if height[start] > height[end]:
                end -= 1
            elif height[start] < height[end]:
                start += 1
            else:
                if height[start + 1] > height[end - 1]:
                    start += 1
                else:
                    end -= 1
        return area
