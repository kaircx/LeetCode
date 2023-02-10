class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=[]
        i=0
        tmp=[]
        while i<len(s):
            m.append(len(tmp))  
            while s[i] in tmp:
                tmp.pop(0)
            tmp.append(s[i])
            i+=1
        m.append(len(tmp))
        if s=="":
            return 0
        else:
            return max(m)
        
        