# O(N) time | O(N) space


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        start = 0
        maxLength = 0
        for i, char in enumerate(s):
            if char in seen:
                start = max(start, seen[char] + 1)
            maxLength = max(maxLength, i - start + 1)
            seen[char] = i
        return maxLength
