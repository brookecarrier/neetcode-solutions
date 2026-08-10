class Solution {
public:
    int characterReplacement(string s, int k) {

        if (s.length() <= k) return s.length();

        vector<int> count(26, 0);
        int left = 0, maxCount = 0, maxLength = 0;

        for (int right = 0; right < s.size(); right++) {
            count[s[right] - 'A']++;
            maxCount = max(count[s[right] - 'A'], maxCount);

            // window size - maxcount is chars to replace
            if ((right - left + 1) - maxCount > k) {
                count[s[left] - 'A']--;
                left++;
            }

            maxLength = max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
};
