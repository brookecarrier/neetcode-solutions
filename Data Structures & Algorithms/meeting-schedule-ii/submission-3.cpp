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

        vector<int> startTimes, endTimes;

        for (auto& interval : intervals) {
            startTimes.push_back(interval.start);
            endTimes.push_back(interval.end);
        }

        sort(startTimes.begin(), startTimes.end());
        sort(endTimes.begin(), endTimes.end());

        int s = 0, e = 0;
        int rooms = 0, maxRooms = 0;

        while (s < startTimes.size()) {
            if (startTimes[s] < endTimes[e]) {
                rooms++;
                maxRooms = max(rooms, maxRooms);
                s++;
            } else {
                rooms--;
                e++;
            }
        }

        return maxRooms;
      
    }
};
