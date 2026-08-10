class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        unordered_set<int> zeroRows, zeroCols;

        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                if (matrix[i][j] == 0) {
                    zeroRows.insert(i);
                    zeroCols.insert(j);
                }
            }
        }

        vector<int> allZerosRow(matrix[0].size(), 0);
        for (auto& row : zeroRows) {
            matrix[row] = allZerosRow;
        }

        for (auto&col : zeroCols) {
            for (auto& row : matrix) {
                row[col] = 0;
            }
        }
        
    }
};
