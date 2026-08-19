class Solution:
    def countSubstrings(self, s: str) -> int:
        # same concept as longest substr, just inc count every time you find one

        count = 0
        
        # odd number
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        
        # even number
        for i in range(len(s)):
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        
        return count

        