class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        HM = {}

        for n in nums:
            HM[n] = HM.get(n,0) + 1

        bucket = [[] for _ in range(len(nums)+1)]

        for n in HM:
            bucket[HM[n]].append(n)
        
        li = len(bucket)-1
        output = []
        while k > 0:
            if bucket[li]:
                for i in bucket[li]:
                    output.append(i)
                    k -= 1
            li -= 1
        return output