class Solution {
public:
    int missingNumber(vector<int>& nums) {

        int expectedSum = 0;
        for (int i = 0; i < nums.size()+1; i++) {
            expectedSum += i;
        }

        int actualSum = 0;
        for (int num : nums) {
            actualSum += num;
        }

        return expectedSum - actualSum;
    }
};
