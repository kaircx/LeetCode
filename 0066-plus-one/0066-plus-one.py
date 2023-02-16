class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pre=len(digits)
        a=int("".join(map(str, digits)))+1
        return [int(x) for x in str(a)]
        
        
        