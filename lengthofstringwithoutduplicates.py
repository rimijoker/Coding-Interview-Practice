class Solution:
  def lengthOfLongestSubstring(self, s):
    seen = []
    count = 0
    for character in s:
        if character not in seen:
            seen.append(character)
            count += 1


print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10