class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {

        // sort by start time
        sort(intervals.begin(), intervals.end(), [] (const auto& a, const auto&b) {
            return a[0] < b[0];
        });

        int remove = 0;
        int prev_end = intervals[0][1];

        for (int i = 1; i < intervals.size(); i++) {
            // if start time less than prev end time
            if (intervals[i][0] < prev_end) {
                prev_end = min(prev_end, intervals[i][1]);
                remove++;
            } else {
                prev_end = intervals[i][1];
            }
        }

        return remove;
        
    }
};
