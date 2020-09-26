# Recursive Solution
# O(NM) time | O(NM) space


def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False

    cache = [[None for j in range(len(two) + 1)] for i in range(len(one) + 1)]
    return areInterwoven(one, two, three, 0, 0, cache)


def areInterwoven(one, two, three, i, j, cache):
    if cache[i][j] is not None:
        return cache[i][j]

    k = i + j
    if k == len(three):
        return True

    if i < len(one) and one[i] == three[k]:
        cache[i][j] = areInterwoven(one, two, three, i + 1, j, cache)
        if cache[i][j]:
            return True

    if j < len(two) and two[j] == three[k]:
        cache[i][j] = areInterwoven(one, two, three, i, j + 1, cache)
        return cache[i][j]

    cache[i][j] = False
    return False


# O(NM) time | O(NM) space


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[None for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or (
                        dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                    )

        return dp[-1][-1]


# O(NM) time | O(M) space


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False

        previous = [None for _ in range(len(s2) + 1)]

        for i in range(len(s1) + 1):
            current = [None for _ in range(len(s2) + 1)]
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    current[j] = True
                elif i == 0:
                    current[j] = current[j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    current[j] = previous[j] and s1[i - 1] == s3[i + j - 1]
                else:
                    current[j] = (current[j - 1] and s2[j - 1] == s3[i + j - 1]) or (
                        previous[j] and s1[i - 1] == s3[i + j - 1]
                    )
            previous = current[:]

        return current[-1]
