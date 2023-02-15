class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0
        for i in range(len(s)):
            if s[len(s)-i-1]!=" ":
                c+=1
            elif c!=0: 
                return c
        return c       
        