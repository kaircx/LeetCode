import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def over(num):
            if num >= 2**31:
                return num-(num-2**31+1)
            else:
                return num
        if dividend==0:
            return 0
        return over(math.floor(math.floor(abs(dividend)/abs(divisor))*(dividend/abs(dividend))*(divisor/abs(divisor))))
        