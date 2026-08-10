class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # iterate, add to map {nums[i], count++}
        # create array of arrays length n, add counts
        # return top k buckets

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            # get(num, 0) returns the current count if it exists, otherwise 0.
        
        buckets = [[] for _ in range(len(nums)+1)]
        for num, freq in counts.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k: return result
            




