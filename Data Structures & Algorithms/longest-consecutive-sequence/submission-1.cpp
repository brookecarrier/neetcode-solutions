class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        if (nums.size() < 2) return nums.size();

        sort(nums.begin(), nums.end());

        int longest = 1;
        int currLength = 1;
        int currIdx = 1;

        while (currIdx < nums.size()) {
            if (nums[currIdx] == nums[currIdx-1]) {
                currIdx++;
            } else if (nums[currIdx] == nums[currIdx-1]+1) {
                currLength++;
                if (currLength > longest) {
                    longest = currLength;
                }
                currIdx++;
            } else {
                currLength = 1;
                currIdx++;
            }
        }

        return longest;
        
    }
};
