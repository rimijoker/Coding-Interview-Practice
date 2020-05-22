class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first , second, third = float("-inf"), float("-inf"), float("-inf")
        for num in nums:
            if num != first and num != second and num != third:
                if num > first :
                    third = second
                    second = first
                    first = num
                elif num > second:
                    third = second
                    second = num
                elif num > third:
                    third = num
        return max(nums) if first == float("-inf") or second == float("-inf") or third == float("-inf") else third