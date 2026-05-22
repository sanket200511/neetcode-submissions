class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HM = {}
        needed = 0

        for ind,val in enumerate(nums):
            needed = target - val
            if needed in HM:
                return [HM[needed],ind]
            HM[val] = ind

        