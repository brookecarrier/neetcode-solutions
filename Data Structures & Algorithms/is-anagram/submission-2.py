class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make array of ascii, should cancel out to 0s

        ord('a')

        if len(s) != len(t): return False

        count = [0 for _ in range(26)]

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for letter in count:
            if letter != 0:
                return False
        
        return True

