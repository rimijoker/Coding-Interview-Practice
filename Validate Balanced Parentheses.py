class Solution:
    def isValid(self, s):
        n=0
        for c in s:
            if (c == "(" or c == "[" or c == "{"):
                n +=1
            elif(c == ")" or c == "}" or c == "]"):
                n-=1
        if n == 0:
            return True
        else:
            return False 

    # Fill this in.

# Test Program
s = "()(){(())" 
# should return False
print((Solution().isValid(s)))

s = "{{{}}}}"
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
