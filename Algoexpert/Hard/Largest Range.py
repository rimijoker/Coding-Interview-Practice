class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)
        best_range = None

        for num in num_set:
            current_range = []
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                current_range.append(current_num)
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                current_range.append(current_num)
                if current_streak > longest_streak:
                    longest_streak = current_streak
                    best_range = current_range[:]

        print(best_range)
        return longest_streak
