class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        l = 0
        r = len(self.nums) 

        while l < r:
            mid = (l + r) // 2
            if self.nums[mid] < num:
                l = mid + 1
            else:
                r = mid
        
        self.nums.insert(l, num)
        

    def findMedian(self) -> float:

        midIdx = len(self.nums) // 2

        if len(self.nums) % 2 == 1:
            return float(self.nums[midIdx])
        else:
            return (self.nums[midIdx - 1] + self.nums[midIdx]) / 2

        
        