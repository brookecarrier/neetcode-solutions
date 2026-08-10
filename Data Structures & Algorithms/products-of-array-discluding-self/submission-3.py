class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # make left product - from l to r
        # make right product - from r to l
        # multiply by each other for final array 

        left_products = [1]
        right_products = [1]
        final_products = []

        current_product = 1
        for i in range(1, len(nums)):
            current_product *= nums[i-1]
            left_products.append(current_product)

        current_product = 1
        for i in range(len(nums)-2, -1, -1):
            current_product *= nums[i+1]
            right_products.append(current_product)
        right_products.reverse()

        for i in range(len(nums)):
            final_products.append(left_products[i] * right_products[i])
        
        return final_products

