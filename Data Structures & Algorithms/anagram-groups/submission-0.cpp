class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        if (strs.size() < 2) return {strs};

        unordered_map<string, vector<string>> map;
        for (string str : strs) {
            string key = str;
            sort(key.begin(), key.end());
            map[key].push_back(str);
        }

        vector<vector<string>> output;
        for (const auto& pair : map) {
            output.push_back(pair.second);
        }

        return output;
    }
};
