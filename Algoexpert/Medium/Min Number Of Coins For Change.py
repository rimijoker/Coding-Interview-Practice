# O(NM) time | O(N) space


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        minimum_number_of_coins = [0] + [float("inf")] * (amount + 1)

        for coin in coins:
            for current_amount in range(coin, amount + 1):
                # the new min may be min of coins required to make up
                # balance(taking out the value of coin in current amount) +1 (adding value of coin)
                balance = current_amount - coin
                minimum_number_of_coins[current_amount] = min(
                    minimum_number_of_coins[current_amount],
                    minimum_number_of_coins[balance] + 1,
                )

        return (
            minimum_number_of_coins[amount]
            if minimum_number_of_coins[amount] != float("inf")
            else -1
        )
