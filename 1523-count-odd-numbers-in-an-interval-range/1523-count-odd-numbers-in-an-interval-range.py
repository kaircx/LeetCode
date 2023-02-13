class Solution:
    def countOdds(self, low: int, high: int) -> int:
        a=(high-low+1)
        if a%2==0:
            return int(a/2)
        else:
            if low%2==0:
                return int(a/2)
            else:
                return int(a/2)+1