class Solution:
    def countOdds(self, low: int, high: int) -> int:
        a= int((high-low+1)/2)
        if (high-low)%2!=0:
            return a
        else:
            if low%2==0:
                return a
            else:
                return a+1