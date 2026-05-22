class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ls = 0
        maxi = 0

        for num in s:
            if num-1 not in s:
                maxi = 0
                n = num
                while n in s:
                    maxi += 1
                    n += 1
                ls = max(ls,maxi)
        return ls
            