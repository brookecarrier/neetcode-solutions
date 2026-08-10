class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {

    // build adjacency list
    vector<vector<int>> graph(numCourses);

    for (auto& pair : prerequisites) {
        graph[pair[1]].push_back(pair[0]);
    }     

    // states: 0 unvisited, 1 in current dfs, 2 completed
    vector<int> states(numCourses, 0);

    // dfs for each course
    for (int i = 0; i < numCourses; i++) {
        if (hasCycle(graph, states, i)) return false;
    }

    return true;
        
    }

private:
    bool hasCycle(vector<vector<int>>& graph, vector<int>& states, int course) {
        if (states[course] == 1) return true;
        if (states[course] == 2) return false;

        states[course] = 1; // currently visiting

        for (int neighbor : graph[course]) {
            if (hasCycle(graph, states, neighbor)) return true;
        }

        states[course] = 2; // made it through
        return false;
    }    
};
