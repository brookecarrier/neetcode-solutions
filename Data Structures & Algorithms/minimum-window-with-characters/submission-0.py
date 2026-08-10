class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or (len(t) > len(s)):
            return ""
            
        dict_t = Counter(t)
        required = len(dict_t) # unique chars

        window_counts = {}
        formed = 0 # unqiue chars matched
        l, r = 0, 0

        min_len = float('inf')
        min_left = 0

        while r < len(s):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            # check if current char completes freq for that char
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            
            # try to shrink window from left if all chars found in window
            while l <= r and formed == required:
                char = s[l]

                # update min window if smaller
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    min_left = l
                
                # remove left char and see if window still valid
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                
                l += 1
            
            r += 1
        
        return "" if min_len == float('inf') else s[min_left:min_left+min_len]


 



        