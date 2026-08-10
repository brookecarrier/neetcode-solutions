class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {

        vector<int> list;
        // boundaries
        int top = 0;
        int bottom = matrix.size() - 1;
        int left = 0;
        int right = matrix[0].size() - 1;

        while (top <= bottom && left <= right) {
            // left to right
            for (int col = left; col <= right; col++) {
                list.push_back(matrix[top][col]);
            }
            top++;

            // top to bottom
            for (int row = top; row <= bottom; row++) { 
                list.push_back(matrix[row][right]);
            }
            right--;

            // right to left
            if (top <= bottom) {
                for (int col = right; col >= left; col--) {
                    list.push_back(matrix[bottom][col]);
                }
            }
            bottom--;

            // bottom to top
            if (left <= right) {
                for (int row = bottom; row >= top; row--) { 
                    list.push_back(matrix[row][left]);
                }
            }
            left++;
            
        }

        return list;
        
    }
};
