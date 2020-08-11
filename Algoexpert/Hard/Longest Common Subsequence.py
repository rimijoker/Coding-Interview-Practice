"""This solution can be optimized to O(nm) time and space
by using a matrix of shape m, n with a data structure
like a list which stores values like current char, len and revious index.
Ex- [ , , , ] *n*m"""

# O(mn * min(m, n)) time & space because of string concatenation
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        l1, l2 = len(text1), len(text2)
        previous = ["" for _ in range(l1 + 1)]

        for i in range(1, l2 + 1):
            current = ["" for _ in range(l1 + 1)]
            for j in range(1, l1 + 1):
                if text2[i - 1] == text1[j - 1]:
                    current[j] = previous[j - 1] + text1[j - 1]
                else:
                    current[j] = max(current[j - 1], previous[j], key=len)

            previous = current[:]

        return previous[-1]
