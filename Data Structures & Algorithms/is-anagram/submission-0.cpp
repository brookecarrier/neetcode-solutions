class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> freq;

        for (char ch : s) {
            freq[ch]++;
        }

        for (char ch : t) {
            freq[ch]--;
        }

        //auto& — automatic type deduction plus reference to original
        // check if all freqs are 0
        for (auto& pair : freq) {
            if (pair.second != 0) return false;
        }

        return true;

        return false;

        
    }
};
