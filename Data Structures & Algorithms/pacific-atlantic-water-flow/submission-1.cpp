class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {

        int rows = heights.size();
        int cols = heights[0].size();

        vector<vector<bool>> pacific(rows, vector<bool>(cols, false));
        vector<vector<bool>> atlantic(rows, vector<bool>(cols, false));

        vector<vector<int>> results;

        // reverse dfs for pacific left col cells
        for (int i = 0; i < rows; i++) {
            dfs(heights, pacific, i, 0, rows, cols);
        }
        // reverse dfs for pacific top row cells
        for (int j = 0; j < cols; j++) {
            dfs(heights, pacific, 0, j, rows, cols);
        }
        // reverse dfs for atlantic right col cells
        for (int i = 0; i < rows; i++) {
            dfs(heights, atlantic, i, cols-1, rows, cols);
        }
        // reverse dfs for atlantic bottom row cells
        for (int j = 0; j < cols; j++) {
            dfs(heights, atlantic, rows-1, j, rows, cols);
        }

        // compare
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    results.push_back({i,j});
                }
            }
        }

        return results;
        
    }

private:
    void dfs(vector<vector<int>>& heights,  vector<vector<bool>>& visited, int i, int j, int rows, int cols) {
        visited[i][j] = true;

        // left cell
        if (j-1 >= 0 && !visited[i][j-1] && heights[i][j-1] >= heights[i][j]) {
            dfs(heights, visited, i, j-1, rows, cols);
        }
        // top cell
        if (i-1 >= 0 && !visited[i-1][j] && heights[i-1][j] >= heights[i][j]) {
            dfs(heights, visited, i-1, j, rows, cols);
        }
        // right cell
        if (j+1 < cols && !visited[i][j+1] && heights[i][j+1] >= heights[i][j]) {
            dfs(heights, visited, i, j+1, rows, cols);
        }
        // bottom cell
        if (i+1 < rows && !visited[i+1][j] && heights[i+1][j] >= heights[i][j]) {
            dfs(heights, visited, i+1, j, rows, cols);
        }
    }
};
