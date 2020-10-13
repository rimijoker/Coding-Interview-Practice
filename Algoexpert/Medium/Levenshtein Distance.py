# O(NM) time | (min(N, M)) space


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_length = len(word1)
        word2_length = len(word2)

        previous = [i for i in range(word1_length + 1)]

        for word2Idx in range(1, word2_length + 1):
            current = [word2Idx] * (word1_length + 1)
            for word1Idx in range(1, word1_length + 1):
                isEqual = 0 if word1[word1Idx - 1] == word2[word2Idx - 1] else 1
                current[word1Idx] = min(
                    previous[word1Idx] + 1,
                    current[word1Idx - 1] + 1,
                    previous[word1Idx - 1] + isEqual,
                )
            previous = current[:]
        return previous[-1]
