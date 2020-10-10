# O(NK) time | O(N) space


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        if k < 1 or n < 2:
            return 0

        if (2 * k) >= n:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)

        previousProfits = [0 for price in prices]

        for transaction in range(1, k + 1):
            maxThusFar = float("-inf")
            currentProfits = [0 for price in prices]
            for day in range(1, n):
                maxThusFar = max(maxThusFar, previousProfits[day - 1] - prices[day - 1])
                currentProfits[day] = max(
                    currentProfits[day - 1], maxThusFar + prices[day]
                )
            previousProfits = currentProfits[:]

        return currentProfits[-1]
