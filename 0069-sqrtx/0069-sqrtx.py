class Solution:
    def mySqrt(self, x: int) -> int:
        i=1
        while True:
            if round(x//i)==i:
                return i
            elif round(x//i)==i-1:
                return i-1
            i+=1
            
            
            
            
        