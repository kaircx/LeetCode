class Solution:
    def climbStairs(self, n: int) -> int:
        tmp =[1,2]
        for i in range(n):
            a=tmp[i-1+2]+tmp[i-2+2]
            tmp.append(a)
        return tmp[len(tmp)-3]
            
            
            
            
            
            