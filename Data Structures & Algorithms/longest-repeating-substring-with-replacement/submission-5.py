class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # for window track if max freq char + k <= window len
        # if so expand r
        # if not shrink l

        chars = {}
        maxFreq = 0
        maxLen = 0
        l = 0

        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            maxFreq = max(maxFreq, chars[s[r]])

            if (r - l + 1) - maxFreq > k:
                chars[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen

        