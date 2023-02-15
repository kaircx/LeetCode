import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high=0
        low=10000
        a=[]
        for i,price in enumerate(prices):
            if price<low:
                low = price
                high=0
            elif price>high:
                high = price
                a.append((high-low))
        if len(a)<=0:
            return 0
        else:
            return max(a)
            
            
