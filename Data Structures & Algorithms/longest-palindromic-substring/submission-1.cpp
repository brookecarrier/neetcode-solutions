class Solution {
public:
    string longestPalindrome(string s) {

        string palindrome = "";

        for (int left = 0; left < s.length(); left++) {
            int right = s.size() - 1;

            while (right >= left) {
                if (s[left] == s[right] && right - left + 1 > palindrome.length() && isPalindrome(s, left, right)) {
                    palindrome = s.substr(left, right - left + 1);
                }
                right--;
            }
        }

        return palindrome;
        
    }

private:
    bool isPalindrome(string s, int l, int r) {
        while (l < r) {
            if (s[l] != s[r]) return false;
            l++;
            r--;
        }

        return true;
    }
};
