class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        HM = {}

        for st in s:
            HM[st] = HM.get(st,0) + 1
        
        for st in t:
            if not HM.get(st):
                return False
            elif HM[st] > 0:
                HM[st] -= 1
        
        if sum(list(HM.values())) == 0:
            return True
        return False