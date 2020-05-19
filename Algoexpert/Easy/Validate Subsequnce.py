class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        if len(s) == 0 or len(t) == 0: return True
        idx=0
        for i in range(0, len(t)):
            if t[i] == s[idx]:
                idx += 1
                if idx == len(s):
                    return True
        return False