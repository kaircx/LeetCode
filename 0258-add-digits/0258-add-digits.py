class Solution:
    def addDigits(self, num: int) -> int:
        tmp=11
        while tmp>=10:
            tmp=0
            num=str(num)
            for i in num:
                tmp+=int(i)
            num=tmp
        return tmp