class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {

        // tree must have n-1 edges
        if (edges.size() != n-1) return false;

        // list of neighbors
        vector<vector<int>> graph(n);    

        // build adjacency list
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        // visited keep track
        vector<bool> visited(n, false);

        // start dfs from node 0
        if (hasCycle(graph, visited, 0, -1));

        // check if all nodes were visited
        for (bool v : visited) {
            if (!v) return false;
        }

        return true;

    }

private:
    bool hasCycle(vector<vector<int>>& graph, vector<bool>& visited, int node, int parent) {
        visited[node] = true;

        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                hasCycle(graph, visited, neighbor, node);
            } else if (neighbor != parent) {
                return true;
            }
        }

        return false;
    }    
};
