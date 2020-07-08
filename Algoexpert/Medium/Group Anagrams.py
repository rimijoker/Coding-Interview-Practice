class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            if key not in ans:
                ans[key] = [s]
            else:
                ans[key].append(s)

        return ans.values()
