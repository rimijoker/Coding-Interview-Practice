class Solution: 
    def longestPalindrome(self, s):
        if s is '':
            return s
        self.maxLength = 0
        self.start = 0
    
        for i in range(len(s)):
            # Check for odd length palindromes
            self.expandFromCenter(s,i,i)
            # Check for even length palindromes
            self.expandFromCenter(s,i,i+1)
        return s[self.start:self.start+self.maxLength]
    
    # Helper function to expand a substring around a central character or characters.
    def expandFromCenter(self, s, low, high):
        while low > -1 and high < len(s) and s[low] == s[high]:
            low -= 1
            high += 1
        # Check to see if we found a longer palindrome than our current counter.
        # Adjust maxLength and start index to counteract increment from while loop. 
        if self.maxLength < high-low-1: 
            self.maxLength = high-low-1
            self.start = low+1  

         
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
