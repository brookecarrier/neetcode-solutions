class PrefixTree {
private:
    struct TreeNode {
        TreeNode* children[26] = {nullptr};
        bool isEnd = false;
    };

    TreeNode* root;

public:
    PrefixTree() {
        root = new TreeNode();
    }
    
    void insert(string word) {
        TreeNode* node = root;
        for (char c : word) {
            int index = c - 'a';
            if (!node->children[index]) {
                node->children[index] = new TreeNode();
            }
            node = node->children[index];
        }

        node->isEnd = true;
    }
    
    bool search(string word) {
        TreeNode* node = root;
        for (char c : word) {
            int index = c - 'a';
            if(!node->children[index]) return false;
            node = node->children[index];
        }

        return node->isEnd;
    }
    
    bool startsWith(string prefix) {
        TreeNode* node = root;
        for (char c : prefix) {
            int index = c - 'a';
            if (!node->children[index]) return false;
            node = node->children[index];
        }

        return true;
    }
};
