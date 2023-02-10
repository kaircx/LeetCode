# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        d=2
        while True:
            if isBadVersion(int(n)):
                if not isBadVersion(n-1):
                    return int(n)
                else:
                    n-=n/d
            else:
                if isBadVersion(n+1):
                    return int(n+1)
                else:
                    n+=n/d
                    d=d*d

            
