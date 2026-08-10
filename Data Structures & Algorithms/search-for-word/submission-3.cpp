class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if (dfs(board, word, 0, i, j)) {
                    return true;
                }
            }
        }

        return false;
        
    }

private:
    bool dfs(vector<vector<char>>& board, string& word, int idx, int i, int j) {

        // if you've reached end of word
        if (idx == word.size()) return true;

        // check bounds and char match
        if (i < 0 || i >= board.size() || 
            j < 0 || j >= board[0].size() ||
            board[i][j] != word[idx]) {
                return false;
        }

        // temp. replace char as visited
        char temp = board[i][j];
        board[i][j] = '#';

        // try all neighbors
        bool found = dfs(board, word, idx+1, i+1, j) ||
                     dfs(board, word, idx+1, i-1, j) ||
                     dfs(board, word, idx+1, i, j+1) ||
                     dfs(board, word, idx+1, i, j-1);

        // replace back to OG
        board[i][j] = temp;

        return found;
    }
};
