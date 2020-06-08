def maxSubsetSumNoAdjacent(nums):
    inclusive, exclusive = nums[0], 0
    for idx in range(1, len(nums)):
        temp = inclusive
        inclusive = max(inclusive, exclusive + nums[idx])
        exclusive = temp
    return inclusive


print(maxSubsetSumNoAdjacent([2, 3, 10, 13, 7, 12]))
