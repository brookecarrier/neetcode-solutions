class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # init l and r to be 0
        # add letters to set
        # update maxLen
        # move r until letter found in set
        # move l until letter not found?

        charSet = set()
        maxLen = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            maxLen = max(maxLen, r - l + 1)

        return maxLen
        