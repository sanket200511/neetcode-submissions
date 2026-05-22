class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        HM = defaultdict(list)

        for s in strs:
            temp = [0]*26
            for i in s:
                temp[ord(i) - ord("a")] += 1
            t = tuple(temp)
            HM[t].append(s)
        return list(HM.values())