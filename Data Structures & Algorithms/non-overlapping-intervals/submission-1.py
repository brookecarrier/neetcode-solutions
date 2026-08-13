class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end time
        # iterate thru, if [1] start time < [0] end time, remove it and inc count
        # if not, update current end

        intervals.sort(key=lambda x: x[1])
        prev_end = intervals[0][1]
        count = 0

        for interval in intervals[1:]:
            if interval[0] < prev_end:
                count += 1
            
            else:
                prev_end = interval[1]
        
        return count


        