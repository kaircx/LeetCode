class Solution:
    def tribonacci(self, n: int) -> int:
        tmp =[0,1,1]
        if n >=3:
            for i in range(n-2):
                tmp.append(tmp[i]+tmp[i+1]+tmp[i+2]) 
        return tmp[n]
            
        