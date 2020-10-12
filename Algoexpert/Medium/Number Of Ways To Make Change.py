# O(NM) time | O(N) space


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        combo = [1] + [0] * (amount)
        for coin in coins:
            for current_amount in range(coin, amount + 1):
                combo[current_amount] += combo[current_amount - coin]
        return combo[-1]
