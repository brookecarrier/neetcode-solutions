class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])

        res = []
        res.append(intervals[0])

        for start, end in intervals:
            prevEnd = res[-1][1]
            if start <= prevEnd:
                res[-1][1] = max(prevEnd, end)
            else:
                res.append([start, end])
        
        return res

            
            
            

        