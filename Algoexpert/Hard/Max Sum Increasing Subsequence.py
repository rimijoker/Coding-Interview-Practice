# Time O(N^2) | Space O(N)


class Solution:
    def maxSumIncreasingSubsequence(self, array):
        sums = array[:]
        sequence = [None for i in array]
        max_sum_idx = 0
        for i in range(len(array)):

            current_num = array[i]

            for j in range(i):

                previous_num = array[j]
                if current_num > previous_num and current_num + sums[j] > sums[i]:
                    sums[i] = current_num + sums[j]
                    sequence[i] = j
            if sums[max_sum_idx] < sums[i]:
                max_sum_idx = i

        return (sums[max_sum_idx], self.buildSequence(array, sequence, max_sum_idx))

    def buildSequence(self, array, sequence, current_idx):
        ans = []
        while current_idx is not None:
            ans.append(array[current_idx])
            current_idx = sequence[current_idx]
        return list(reversed(ans))


ans = Solution()
print(ans.maxSumIncreasingSubsequence([1, 10, 3, 2, 15, 25, 4]))
