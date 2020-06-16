class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # O(n) space with rolling array

        l1, l2 = len(word1), len(word2)
        previous = [i for i in range(0, l2 + 1)]

        for char_in_word1 in range(1, l1 + 1):
            current = [char_in_word1] * (l2 + 1)
            for char_in_word2 in range(1, l2 + 1):
                current[char_in_word2] = min(
                    current[char_in_word2 - 1] + 1,
                    previous[char_in_word2 - 1] + (word1[char_in_word1 - 1] != word2[char_in_word2 - 1]),
                    previous[char_in_word2] + 1,
                )
            previous = current[:]

        return previous[-1]
