class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
		# store results in list
        indices = []
		# store lenth of string p since this is reused multiple times
        length_p = len(p)

		# check if p is longer than s, if yes, return empty list
        if length_p > len(s):
            return []

        # create baseline for p by counting the characters in p (26 possible characters)
		# (similar to storing the counts in a dictionary)
        counter_p = [0] * 26
        for c in p:
			# convert each character to its index by calculating the int value and subtracting 97
			# a = 97 -> a-97 = 0
			# b = 98 -> b-97 = 1
			# etc.
            counter_p[ord(c) - 97] += 1

        # initialize counter with the first characters
        counter = [0] * 26
        for i in range(length_p - 1):
            counter[ord(s[i]) - 97] += 1

        # enumerate through remaining characters and compare to baseline (counter_p)
		# use enumerator to get both the index we need for removing the first character and
		# the character we want to add (we are starting with the first character after the once
		# that were initialized above (if len(p)=3, we start at the 3rd character)
        for i, c in enumerate(s[length_p - 1:]):
			# add current character
            counter[ord(c) - 97] += 1
			# compare to baseline
            if counter_p == counter:
                indices.append(i)
			# remove character
            counter[ord(s[i]) - 97] -= 1

        return indices