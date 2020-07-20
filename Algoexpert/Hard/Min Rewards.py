# O(n) time | O(1) space
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        rst = 1
        up = 1
        down = peak = 0
        for i in range(1, len(ratings)):
            # if rising, then update up/peak and clear down
            if ratings[i] > ratings[i - 1]:
                up += 1
                peak = up
                down = 0
                rst += up
            # if equal, then add 1 and clear up/down/peak
            elif ratings[i] == ratings[i - 1]:
                up = 1
                down = 0
                peak = 0
                rst += 1
            # if declining, then update down and clear up
            else:
                up = 1
                down += 1
                rst += down
                # if peak is not large enough, then we need to make peak larger
                if down >= peak:
                    rst += 1
        return rst


# O(n) time | O(n) space
def minRewards(score):
    rewards = [1 for _ in score]
    for i in range(1, len(score)):
        if score[i] > score[i - 1]:
            rewards[i] = rewards[i - 1] + 1
    for i in reversed((range(len(score) - 1))):
        if score[i] > score[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)
