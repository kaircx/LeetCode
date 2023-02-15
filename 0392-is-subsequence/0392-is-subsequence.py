class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s=list(s)
        if len(s)==0:
            return True
        for i in range(len(t)):

            print(s[0],t[i])
            if t[i]==s[0]:
                s.pop(0)
            if len(s)==0:
                return True

        else:
            return False

