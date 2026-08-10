class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        // base case
        if (nums.size() == 2) return {0, 1};
      
        // num, idx
        unordered_map<int, int> map;
        int complement;

        for (int i = 0; i < nums.size(); i++) {
            complement = target - nums[i];
            if (map.find(complement) != map.end()) {
                return {map[complement], i};
            } else {
                map.insert({nums[i], i});
            }

        }


        
    }
};
