class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size()-1;
        int maxArea = 0;
        int currArea;

        while (left < right) {
            if (heights[left] <= heights[right]) {
                currArea = heights[left] * (right - left);
                if (currArea > maxArea) {
                    maxArea = currArea;
                } 
                left++;
            } else {
                currArea = heights[right] * (right - left);
                if (currArea > maxArea) {
                    maxArea = currArea;
                }
                right--;
            }
        }

        return maxArea;
    }
};
