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

        sort(starts.begin(), starts.end());
        sort(ends.begin(), ends.end());

        int currentMeetings = 0;
        int maxOverlaps = 0;
        int i = 0;
        int j = 0;

        while (i < starts.size()) {
            if (starts[i] < ends[j]) {
                currentMeetings++;
                i++;
            } else {
                currentMeetings--;
                j++;
            }
            maxOverlaps = max(currentMeetings, maxOverlaps);
        }

        return maxOverlaps;

    }
};
