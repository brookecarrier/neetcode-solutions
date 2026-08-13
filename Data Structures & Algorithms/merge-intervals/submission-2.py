class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort based on start time
        # go through intervals, if one is fully before the next, append to result
        # if not, merge

        result = []

        intervals.sort() 
        current = intervals[0]

        for interval in intervals[1:]:
            if interval[0] > current[1]:
                result.append(current)
                current = interval
            else:
                current[1] = max(current[1], interval[1])

        result.append(current)

        return result