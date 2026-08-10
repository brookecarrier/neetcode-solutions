class Solution {
    vector<vector<int>> result;
    vector<int> current;

    void backtrack(const vector<int>& nums, int target, int start) {
        if (target == 0) {
            result.push_back(current);
            return;
        }
        if (target < 0) return;

        for (int i = start; i < nums.size(); i++) {
            current.push_back(nums[i]);
            backtrack(nums, target - nums[i], i);
            current.pop_back();
        }
    }


public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {

        backtrack(nums, target, 0);
        return result;
        
    }
};
