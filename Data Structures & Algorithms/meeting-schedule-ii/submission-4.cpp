/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {

        if (intervals.size() <= 1) return intervals.size();

        vector<int> starts, ends;

        for (const auto& interval : intervals) {
            starts.push_back(interval.start);
            ends.push_back(interval.end);
        }

        // sort both
        sort(starts.begin(), starts.end());
        sort(ends.begin(), ends.end());

        int days = 0;
        int e = 0;

        for (int i = 0; i < intervals.size(); i++) {
            if (starts[i] < ends[e]) days++;
            else e++;
        }

        return days;
        
    }
};
