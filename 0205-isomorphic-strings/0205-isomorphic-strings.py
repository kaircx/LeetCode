class Solution:
    def isIsomorphic(self, s, t):
        def check(key,dic):
            if key in dic:
                dic[key]+=1
            else:
                dic[key]=1
            return dic
        dictt={}
        dicts={}
        for i in range(len(s)):
            dicts=check(s[i],dicts)
            dictt=check(t[i],dictt)
            if list(dictt.values())!=list(dicts.values()):
                return False
        return True
        