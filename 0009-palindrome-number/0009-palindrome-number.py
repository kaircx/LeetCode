class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=list(str(x))
        for i in range(int(len(a)/2)):
            if a.pop(0)!=a.pop(-1):
                return False
        return True
            