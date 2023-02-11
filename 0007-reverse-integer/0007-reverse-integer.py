class Solution:
    def reverse(self, x: int) -> int:
        x=list(str(x))
        x.reverse()
        if x[-1]=="-":
            x.insert(0,x.pop(-1))
        answer= int("".join(x))
        if answer <=2**31 and answer>=-2**31:
            return answer
        return 0