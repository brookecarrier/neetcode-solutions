class Solution {
public:
    int rob(vector<int>& nums) {

        if (nums.size() <= 2) return *max_element(nums.begin(), nums.end());

        return max(robLinear(nums, 0, nums.size()-1), robLinear(nums, 1, nums.size()));

    }

private:
    int robLinear(vector<int>& nums, int s, int e) {

        int prev1 = 0;
        int prev2 = 0;

        for (int i = s; i < e; i++) {
            int current = max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }    
};
