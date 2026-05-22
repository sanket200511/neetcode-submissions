class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        for i in range(len(nums)-1):
            result[i+1] = result[i]*nums[i]
        temp = 1
        for i in range(len(nums)-1,0,-1):
            result[i-1] *= temp*nums[i]
            temp *= nums[i]
        return result