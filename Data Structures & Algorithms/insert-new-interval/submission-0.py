class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find where new start is greater than old starts
        # keep idx
        # find merged start by working backwards until interval where it's greater than end is found
        # find merged end by working forwards and finding where its smaller than next start

        output = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1

        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        output.append(newInterval)

        while i < n:
            output.append(intervals[i])
            i += 1
        
        return output


        