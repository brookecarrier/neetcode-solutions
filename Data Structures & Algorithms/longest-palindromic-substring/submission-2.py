class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        # iterate throu using l and r pointers
        # if palindrome, update longest to be max of itself and palindrome

        for i in range(len(s)):
            # odd
            curr = ""
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr = s[l:r+1]
                if len(curr) > len(longest):
                    longest = curr
                l -= 1
                r += 1
            
            # even
            curr = ""
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr = s[l:r+1]
                if len(curr) > len(longest):
                    longest = curr
                l -= 1
                r += 1


        return longest
        