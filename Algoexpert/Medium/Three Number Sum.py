class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        out = []
        nums.sort()
        length = len(nums)
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            
            l, r = i + 1, length - 1
            while l<r:
                total =  nums[i] + nums[l] + nums[r]
                
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    out.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return out