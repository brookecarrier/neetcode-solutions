class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        if (nums.size() <= k) return nums;

        // <num, freq>
        unordered_map<int, int> map;
        for (int num : nums) {
            map[num]++;
        }

        //<type, container, comparator>
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> q;

        for (const auto& pair : map) {
            q.push(make_pair(pair.second, pair.first));
            if (q.size() > k) {
                q.pop();
            }
        }

        vector<int> output;
        while (!q.empty()) {
            output.push_back(q.top().second);
            q.pop();
        }

        return output;
    }
};
