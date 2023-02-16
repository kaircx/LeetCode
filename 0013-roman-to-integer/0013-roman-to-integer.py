class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        y = 0
        for i in s[::-1]: 
            if y <= dict[i] or y == 0:
                sum += dict[i]
                y = dict[i]
            else:
                sum -= dict[i]
        return sum