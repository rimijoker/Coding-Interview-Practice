class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def kadane(gen):
            # Maximum non-empty subarray sum
            ans = -30000
            cur = 0
            for x in gen:
                cur = x + max(cur, 0)
                ans = max(ans, cur)
            return ans

        S = sum(A)
        ans1 = kadane(iter(A))
        ans2 = S + kadane(-A[i] for i in range(1, len(A)))
        ans3 = S + kadane(-A[i] for i in range(len(A) - 1))
        return max(ans1, ans2, ans3)