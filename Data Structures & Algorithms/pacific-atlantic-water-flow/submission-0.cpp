class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size();
        int n = heights[0].size();

        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
        vector<vector<int>> result;

        // dfs for pacific
        for (int i = 0; i < m; i++) dfs(heights, pacific, i, 0, m, n);
        for (int j = 0; j < n; j++) dfs(heights, pacific, 0, j, m, n);

        // atlantic
        for (int i = 0; i < m; i++) dfs(heights, atlantic, i, n-1, m, n);
        for (int j = 0; j < n; j++) dfs(heights, atlantic, m-1, j, m, n);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    result.push_back({i, j});
                }
            }
        }

        return result;
        
    }

private:
    void dfs(vector<vector<int>>& heights, vector<vector<bool>>& visited, int i, int j, int m, int n) {
        visited[i][j] = true;

        // left
        if (j > 0 && !visited[i][j-1] && heights[i][j-1] >= heights[i][j]) dfs(heights, visited, i, j-1, m, n);
        // right
        if (j < n-1 && !visited[i][j+1] && heights[i][j+1] >= heights[i][j]) dfs(heights, visited, i, j+1, m, n);
        // top
        if (i > 0 && !visited[i-1][j] && heights[i-1][j] >= heights[i][j]) dfs(heights, visited, i-1, j, m, n);
        // bottom
        if (i < m-1 && !visited[i+1][j] && heights[i+1][j] >= heights[i][j]) dfs(heights, visited, i+1, j, m, n);



        
    } 

};
