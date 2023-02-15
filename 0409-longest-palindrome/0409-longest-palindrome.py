class Solution:
    def longestPalindrome(self, s: str) -> int:
        dicta={}
        r=0
        f=0
        for i in range(len(s)):
            f+=1
            if s[i] in dicta:
                dicta[s[i]]+=1
                if dicta[s[i]]%2==0:
                    r+=1
                    f-=2
            else:
                dicta[s[i]]=1
        if f>0:
            return r*2+1
        else:
            return r*2