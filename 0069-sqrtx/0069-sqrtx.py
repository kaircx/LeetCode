class Solution:
    def mySqrt(self, x: int) -> int:
        i=1
        while True:
            c=round(x//i)
            if c==i:
                return i
            elif c==i-1:
                return i-1
            i+=1
            
            
            
            
        