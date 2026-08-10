class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort + 2 pointers
        # iterate l and r based on < or > 0

        output = []      

        nums.sort()

        for i in range (len(nums)-2):
            l = 0
            r = len(nums)-1

            while l != r:
                if l == i:
                    l += 1
                elif r == i:
                    r -= 1
                else:
                    total = nums[l] + nums[i] + nums[r]
                    if total == 0:
                        triplet = [nums[l], nums[i], nums[r]]
                        triplet.sort()
                        if triplet not in output:
                            output.append(triplet)
                        l += 1
                    elif total < 0:
                        l += 1
                    else:
                        r -= 1
        
        return output
                
            



      



        