class Solution:
  def lengthOfLongestSubstring(self, s):
    seen = []
    count = 0
    for character in s:
        if character not in seen:
            seen.append(character)
            count += 1

    return count

 
a= Solution().lengthOfLongestSubstring('abcdeffffffffff')
print(a)
# 10