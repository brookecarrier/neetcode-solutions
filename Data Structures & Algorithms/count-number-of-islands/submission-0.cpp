class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {

        int numIslands = 0;

        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == '1') {
                    numIslands++;
                    markIsland(grid, i, j);
                }
            }
        }

        return numIslands;
        
    }
private:
    void markIsland(vector<vector<char>>& grid, int i, int j) {

        // check conditions
        if (i < 0 || i >= grid.size() ||
            j < 0 || j >= grid[0].size() ||
            grid[i][j] != '1') {
                return;
            }

        grid[i][j] = '#';

        markIsland(grid, i+1, j);
        markIsland(grid, i-1, j);
        markIsland(grid, i, j+1);
        markIsland(grid, i, j-1);

    }
};
