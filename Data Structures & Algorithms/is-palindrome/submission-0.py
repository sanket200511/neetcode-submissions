class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ptr1 = 0
        ptr2 = len(s)-1

        while ptr1 < ptr2:
            if not s[ptr1].isalnum():
                ptr1 += 1
            elif not s[ptr2].isalnum():
                ptr2 -= 1
            elif s[ptr1] == s[ptr2]:
                ptr1 += 1
                ptr2 -= 1
            else:
                return False
        return True  
    