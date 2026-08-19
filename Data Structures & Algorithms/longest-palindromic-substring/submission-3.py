class Solution:
    def longestPalindrome(self, s: str) -> str:
        # calculate max for odd num of letters, and then even num

        maxSubstring = s[0]

        # odd number
        for i in range(len(s)):
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(maxSubstring):
                    maxSubstring = s[l:r+1]
                l -= 1
                r += 1
        
        # even number
        for i in range(len(s)):
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(maxSubstring):
                    maxSubstring = s[l:r+1]                
                l -= 1
                r += 1
        
        return maxSubstring

                


        